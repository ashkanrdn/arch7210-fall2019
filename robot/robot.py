#!/usr/bin/python3

import RPi.GPIO as GPIO
import os
import sys

# Modify PATH so we can import files from elsewhere in this repo
sys.path.append(os.path.dirname(__file__) + "/..")

from nicholas.robot.stepper import Motor, PhysicalAxle
from nicholas.robot.turtlebot import Turtle
from nicholas.robot.wsjsonrpc import JSONRPCWebSocket


GPIO.setmode(GPIO.board)

# Set up the motors
left = Motor(7, 11, 13, 15)
right = Motor(29, 31, 33, 37)

# Set up the axle
microsteps_per_revolution = 400
circumference_of_wheel = 8.71875
distance_between_wheels = 9.5625
axle = PhysicalAxle(left, right, microsteps_per_revolution, circumference_of_wheel, distance_between_wheels, 0.01)

# Create the robot
robot = Turtle(axle)

# Set up the WebSocket connection
ws = JSONRPCWebSocket("wss://arch7210-fall2019.coditect.com/pablo")
ws.set_basic_auth("pablo", "********")

try:
	for request in ws.requests():
		request.exec(robot, ws)

except KeyboardInterrupt:
	pass

finally:
	ws.close()
