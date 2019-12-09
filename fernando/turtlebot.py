import math
import servomotor
from .geometry import Vector

class Turtle:

	def __init__(self, axle):
		self.axle = axle
		self.position = Vector(0, 0)
		self.heading = Vector(1, 0)

	def forward(self, distance):
		self.axle.move(distance)
		self.position = self.position + self.heading * distance

	def backward(self, distance):
		self.axle.move(-distance)
		self.position = self.position + self.heading * -distance

	def left(self, degrees):
		self.axle.rotate(degrees)
		self.heading = self.heading.rotate(degrees)

	def right(self, degrees):
		self.axle.rotate(-degrees)
		self.heading = self.heading.rotate(degrees)

	def goto(self, x, y):
		delta = Vector(x, y) - self.position
		self.left(delta.angle() - self.heading.angle())
		self.forward(delta.magnitude())

	def penup(self):


	def pendown(self):


	
	def drawPolygon(self, num_sides, radius):
		a = 360 / num_sides
		s = math.fabs(radius * math.sin(math.radians(a)) / math.sin((math.pi - math.radians(a)) / 2))
		for _ in range(num_sides):
			self.forward(s)
			self.left(a)
	
	def drawStar(self, num_vertices, radius):
		a = 360 / num_vertices
		s = math.fabs(radius * math.sin(math.pi - math.radians(a)/2) / math.sin(math.radians(a)/4))
		for _ in range(num_vertices):
			self.forward(s)
			self.left(180 - a/2)