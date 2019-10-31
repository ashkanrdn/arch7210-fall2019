import math

class Vector:
	
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Vector(self.x - other.x, self.y - other.y)

	def __mul__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			return Vector(self.x * other, self.y * other)

	def __rmul__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			return Vector(self.x * other, self.y * other)

	def __neg__(self):
		return Vector(-self.x, -self.y)

	def __abs__(self):
		return self.magnitude()

	def __str__(self):
		return f"({self.x}, {self.y})"

	def magnitude(self):
		return math.sqrt(self.x*self.x + self.y*self.y)

	def angle(self):
		return math.degrees(math.atan2(self.y, self.x))
	
	def rotate(self, degrees):
		magnitude = self.magnitude()
		newAngle = math.radians(self.angle() + degrees)
		newX = magnitude * math.cos(newAngle)
		newY = magnitude * math.sin(newAngle)
		return Vector(newX, newY)

	def unitize(self):
		return Vector(1, 0).rotate(self.angle())
