import argparse
import math
import turtle

numBranches = 3
branchSpread = 60
initialBranchLength = 200
minimumBranchLength = 5
branchScalingFactor = 2

class Branch:

	branches = []
	
	def __init__(self, t, d=0):
		self.turtle = t
		self.depth = d

	def length(self):
		return initialBranchLength / (branchScalingFactor ** self.depth)

	# def width(self):
	# 	return 

	# def color(self):

	def branch(self, deflection):
		b = Branch(self.turtle.clone(), self.depth + 1)
		b.turtle.left(deflection)
		self.branches.append(b)
	
	def draw(self):
		length = self.length()
		print(self, length)

		if length < minimumBranchLength:
			self.turtle.dot(minimumBranchLength, '#009900')
			return True

		elif len(self.branches) == 0:
			self.turtle.forward(length)
			for i in range(numBranches):
				self.branch(i * branchSpread / numBranches - branchSpread / 2)
			return False

		# else:
		# 	allDone = False
		# 	for b in self.branches:
		# 		done = b.draw()
		# 		allDone = allDone or done
		# 	return True


screen = turtle.Screen()
screen.tracer(0, 0)

t = turtle.Turtle()
t.hideturtle()
t.setheading(90)

root = Branch(t)
done = False

for i in range(5):
	print(i)
	done = root.draw()
	turtle.update()

turtle.done()