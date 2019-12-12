from base64 import b64encode
from json import JSONDecodeError
from lomond import WebSocket
from lomond.persist import persist


class JSONRPCWebSocket(WebSocket):
	"""A WebSocket client that listens for JSON-RPC requests."""

	def set_basic_auth(self, username, password):
		"""Add an Authorization header to the WebSocket request."""
		assert ":" not in username
		user_pass = f"{username}:{password}"
		basic_credentials = b64encode(user_pass.encode())
		self.add_header("Authorization".encode(), "Basic ".encode() +  basic_credentials)

	def requests(self, persistent=True, **persist_args):
		"""Return an interator"""
		events = persist(self, **persist_args) if persistent else self
		for event in events:
			request = self.get_request(event)
			if request is not None:
				yield request

	def get_request(self, event):
		if event.name == "text":
			try:
				parsed = event.json
				if "method" in parsed.keys():
					return Request(**parsed)

			except JSONDecodeError:
				self.send_error(-32700, "Invalid JSON received")
				return False

			except InvalidRequest as err:
				self.send_error(-32600, err.args[0])
				return False

	
	def send_response(self, response_type, response_data, request_id=None):
		"""Send a JSON-RPC response.
		
		For more info, see https://www.jsonrpc.org/specification#response_object.
		"""
		response = {"jsonrpc": "2.0", response_type: response_data}
		if request_id is not None:
			response["id"] = request_id
		self.send_json(response)

	def send_result(self, result, request_id=None):
		"""Send a successful JSON-RPC response."""
		self.send_response("result", result, request_id)

	def send_error(self, code, message, data=None, request_id=None):
		"""Send an unsuccessful JSON-RPC response.

		For more info, see https://www.jsonrpc.org/specification#error_object.
		"""
		error = {"code": code, "message": message}
		if data is not None:
			error["data"] = data
		self.send_response("error", error, request_id)


class Request:
	"""Represents a JSON-RPC request."""

	def __init__(self, method, params=[], id=None):
		self.method = method
		self.params = params
		self.id = id

		if type(params) not in (dict, list):
			raise InvalidRequest("Parameters must be provided as a structured value")

		if id is not None and type(id) not in (int, str):
			raise InvalidRequest("Request identifier must be a string or integer")

	def exec(self, target, websocket):
		"Executes a method on the target object and responds through the given WebSocket connection."
		try:
			method = getattr(target, self.method)
			if callable(method):
				websocket.send_result("Executing " + self.method, self.id)

				if type(self.params) is dict:
					result = method(**self.params)
				else:
					result = method(*self.params)

				if result is None:
					result = "Completed " + self.method
				
				websocket.send_result(result, self.id)
				return True

			else:
				websocket.send_error(-32601, f"{self.method} is not defined", request_id=self.id)
				return False
			
		except AttributeError:
			websocket.send_error(-32601, f"{self.method} is not defined", request_id=self.id)
			return False

		except Exception as err:
			websocket.send_error(-32000, err.args[0], request_id=self.id)
			return False


class InvalidRequest(Exception):
	pass
