import RPi.GPIO as GPIO
import stepper
import turtlebot
import spirograph
import wsjsonrpc


GPIO.setmode(GPIO.BOARD)

left = stepper.Motor(31, 33, 35, 37)
right = stepper.Motor(7, 11, 13, 15)
axle = stepper.PhysicalAxle(left, right, 3.1770833333, 6.90625)

robot = turtlebot.Turtle(axle)

ws = wsjsonrpc.JSONRPCWebSocket("wss://arch7210-fall2019.appspot.com/example")
ws.set_basic_auth("robot", "********")

try:
	for request in ws.requests():
		request.exec(robot, ws)

finally:
	ws.close()
