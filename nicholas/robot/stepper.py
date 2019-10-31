import RPi.GPIO as GPIO
import math
import time

STEPS_PER_REVOLUTION = 4096

class Motor:
	"""Represents a 28BYJ-48 stepper motor."""

	sequence = [
		[1,0,0,0],
		[1,1,0,0],
		[0,1,0,0],
		[0,1,1,0],
		[0,0,1,0], 
		[0,0,1,1],
		[0,0,0,1],
		[1,0,0,1]
	]

	def __init__(self, pin1, pin2, pin3, pin4):
		self.pins = [pin1, pin2, pin3, pin4]
		self.step = 0
		self._setup()
	
	def _setup(self):
		"""Set up the motor's pins as outputs and initialize them to zero."""
		for pin in self.pins:
			GPIO.setup(pin, GPIO.OUT)
			GPIO.output(pin, 0)

	def _apply(self):
		"""Apply the voltage for the current step to each pin."""
		for pin in range(4):
			GPIO.output(self.pins[pin], self.sequence[self.step][pin])

	def forward(self):
		"""Move the motor forward by one step."""
		self.step += 1
		if self.step >= 8:
			self.step = 0
		self._apply()
	
	def backward(self):
		"""Move the motor backward by one step."""
		self.step -= 1
		if self.step < 0:
			self.step = 7
		self._apply()
	
	def go(self, steps, delay=0.001):
		""" Move the motor by the given number of steps."""
		op = self.backward if steps < 0 else self.forward
		for _ in range(abs(steps)):
			op()
			time.sleep(delay)
		


class Axle:
	"""Represents a pair of stepper motors operating as a single unit."""

	def __init__(self, left, right):
		self.left = left
		self.right = right
	
	def stepForward(self):
		"""Move the axle forward by one step."""
		self.left.backward()
		self.right.forward()
	
	def stepBackward(self):
		"""Move the axle backward by one step."""
		self.left.forward()
		self.right.backward()

	def move(self, steps, delay=0.001):
		"""Move the axle by the given number of steps."""
		op = self.stepForward if steps > 0 else self.stepBackward
		for _ in range(abs(steps)):
			op()
			time.sleep(delay)
	
	def stepLeft(self):
		"""Turn the axle to the left by one step."""
		self.left.forward()
		self.right.forward()
	
	def stepRight(self):
		"""Turn the axle to the right by one step."""
		self.left.backward()
		self.right.backward()
	
	def rotate(self, steps, delay=0.001):
		"""Rotate the axle by moving each end by in opposite directions by the given number of steps."""
		op = self.stepLeft if steps > 0 else self.stepRight
		for _ in range(abs(steps)):
			op()
			time.sleep(delay)
	


class PhysicalAxle(Axle):
	"""Represents a pair of stepper motors connected to wheels of known size that are a known distance apart."""

	def __init__(self, left, right, circumference, track):
		super().__init__(left, right)
		self.circumference = circumference
		self.track = track

	def _distanceToSteps(self, distance):
		return distance * STEPS_PER_REVOLUTION / self.circumference
	
	def _stepsToDistance(self, steps):
		return steps * self.circumference / STEPS_PER_REVOLUTION

	def _degreesToSteps(self, degrees):
		arcLength = math.pi * self.track * degrees / 360
		return self._distanceToSteps(arcLength)

	def _stepsToDegrees(self, steps):
		arcLength = self._stepsToDistance(steps)
		return arcLength * 360 / self.track / math.pi

	def move(self, distance):
		"""Moves the axle by the given distance."""
		calculated_steps = self._distanceToSteps(distance)
		rounded_steps = math.floor(calculated_steps)
		super().move(int(rounded_steps))
		return self._stepsToDistance(calculated_steps - rounded_steps)
	
	def rotate(self, degrees):
		"""Rotates the axle by the given number of degrees."""
		calculated_steps = self._degreesToSteps(degrees)
		rounded_steps = math.floor(calculated_steps)
		super().rotate(int(rounded_steps))
		return self._stepsToDegrees(calculated_steps - rounded_steps)
