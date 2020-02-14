#!/usr/bin/python3

import RPi.GPIO as GPIO
import os
import sys
import servomotor
import eyematrix
import busio
import time
import json

import board


# Modify PATH so we can import files from elsewhere in this repo
sys.path.append(os.path.dirname(__file__) + "/..")

from nicholas.robot.stepper import Motor, PhysicalAxle
from nicholas.robot.turtlebot import Turtle
from nicholas.robot.wsjsonrpc import JSONRPCWebSocket

from lomond.persist import persist

# busio.I2C calls GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)
#GPIO.setmode(GPIO.BCM)
i2c = busio.I2C(board.SCL, board.SDA)

# Set up the motors / GPIO.BCM
left = Motor(4, 17, 27, 22)
right = Motor(5, 6, 13, 26)

# Set up the motors / GPIO.BOARD
#left = Motor(7, 11, 13, 15)
#right = Motor(29, 31, 33, 37)

# Set up the axle
microsteps_per_revolution = 400
circumference_of_wheel = 8.71875
distance_between_wheels = 9.425
#circumference_of_wheel = 8.71875
#distance_between_wheels = 9.5625
axle = PhysicalAxle(left, right, microsteps_per_revolution, circumference_of_wheel, distance_between_wheels, 0.01)

pen = servomotor.ServoPen()
eyes = eyematrix.RobotEyes(i2c,0x70,0x74)

# Create the robot
robot = Turtle(axle, pen, eyes)

# Set up the WebSocket connection
ws = JSONRPCWebSocket("wss://arch7210-fall2019.coditect.com/pablo")
ws.set_basic_auth("pablo", "*************")


# Counter for eyes
blink_count = 0 
tired_count = 0
angry_count = 0
try:
	for event in persist(ws):
		request = ws.get_request(event)
		print(event)
		
		if request is not None:
			blink_count = 0
			tired_count += 1
			angry_count = 0
			
			if request == False or request.exec(robot, ws) == False:
				angry_count += 1
				print(angry_count)
				
				if angry_count > 5:
					eyes.angry()
					
				else: 
					eyes.sad()
			
		elif event.name == "poll":
			if blink_count < 5:
				eyes.blink()
				blink_count += 1
			else:
				eyes.bored()
				tired_count = 0
		
		elif event.name == "text":
			print(tired_count)
			if tired_count > 50:
				eyes.tired()
		
except KeyboardInterrupt:
	pass

finally:
	ws.close()
