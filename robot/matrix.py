from PIL import Image

import busio
import board
from adafruit_ht16k33.matrix import Matrix8x8x2
i2c = busio.I2C(board.SCL, board.SDA)



BLACK = 0
GREEN = 1
RED = 2
YELLOW = 3


def loadImage(path):
	"""Load an image for use on a bicolor LED matrix."""
	image = Image.open(path)
	if image.width != image.height:
		raise Exception("Image must be square")

	matrix = BicolorMatrix(image.width)
	for x in range(image.width):
		for y in range(image.height):
			r, g, b = image.getpixel((x + 0.5, y + 0.5))
			if r > 127 and g > 127:
				matrix.data[y][x] = YELLOW
			elif r > 127:
				matrix.data[y][x] = RED
			elif g > 127:
				matrix.data[y][x] = GREEN
	
	return matrix

class BicolorMatrix:

	def __init__(self, size=8):
		self.data = []
		for x in range(size):
			self.data.append([])
			for y in range(size):
				self.data[x].append(0)
	
	@property
	def size(self):
		return len(self.data)

	def apply(self, ledMatrix):
		for x in range(self.size):
			for y in range(self.size):
				ledMatrix.pixel(x, y, self.data[y][x])
		if not ledMatrix.auto_write:
			ledMatrix.show()

	def flip(self):
		"""Flip the matrix horizontally."""
		flipped = BicolorMatrix(self.size)
		for i in range(self.size):
			flipped.data[i] = self.data[i][::-1]
		return flipped

	def flop(self):
		"""Flip the matrix vertically."""
		flopped = BicolorMatrix(self.size)
		max = self.size - 1
		for x in range(self.size):
			for y in range(self.size // 2):
				flopped.data[y][x] = self.data[max-y][x]
				flopped.data[max-y][x] = self.data[y][x]
		return flopped

	def transpose(self):
		"""Flip the matrix across the diagonal axis from upper right to lower left.""" 
		transposed = BicolorMatrix(self.size)
		max = self.size - 1
		for y in range(self.size):
			for x in range(self.size):
				transposed.data[y][x] = self.data[max-x][max-y]
		return transposed

	def rotateLeft(self):
		"""Rotate the matrix 90 degrees clockwise."""
		return self.transpose().flop()
	
	def rotateRight(self):
		"""Rotate the matrix 90 degrees counterclockwise."""
		return self.transpose().flip()

	def print(self):
		for row in self.data:
			print(row)
			
