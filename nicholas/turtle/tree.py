import argparse
import turtle

class Tree(turtle.Turtle):
	
	left = None
	right = None
	drawn = False

	def __init__(self, position, heading, length=200):
		turtle.Turtle.__init__(self)
		self.hideturtle()
		self.penup()
		self.setposition(position)
		self.setheading(heading)
		self.length = length
		self.pendown()
	
	def draw(self, minBranchLength=5):
		if self.length < minBranchLength:
			self.dot(minBranchLength, '#009900')
			return True
		elif self.left == None or self.right == None:
			self.forward(self.length)
			self.left = Tree(self.position(), self.heading() - 30, self.length * 0.5)
			self.right = Tree(self.position(), self.heading() + 30, self.length * 0.5)
			self.drawn = True
			return False
		else:
			leftDone = self.left.draw(minBranchLength)
			rightDone = self.right.draw(minBranchLength)
			return leftDone and rightDone


screen = turtle.Screen()
screen.tracer(1, 0)

tree = Tree((0, -200), 90, 200)
tree.numBranches = 3
done = False

while not done:
	done = tree.draw(5)

turtle.done()