import RPi.GPIO as GPIO
import stepper
import turtlebot
import spirograph
import time
import math

try:
	GPIO.setmode(GPIO.BOARD)

	left = stepper.Motor(31, 33, 35, 37)
	right = stepper.Motor(7, 11, 13, 15)
	axle = stepper.PhysicalAxle(left, right, 3.1770833333, 6.90625)

	robot = turtlebot.Turtle(axle)

	#robot.drawStar(7, 2)

	spiro = spirograph.Spirograph(robot, 3, 1, 1.5)
	spiro.start()
	time.sleep(5)
	
	more = True
	while more:
		more = spiro.increment(math.radians(1))
		

finally:
	print("done")
	#GPIO.cleanup()