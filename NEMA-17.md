Hooking Up a NEMA-17 Stepper with the L298 Controller
=====================================================

This document describes the electrical connections between a [NEMA-17 stepper motor from Adafruit](https://www.adafruit.com/product/324), an L298N dual H-bridge motor controller, and a [Raspberry Pi 4](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/).

## Connecting the motor to the controller
- Connect the yellow wire to OUT1
- Connect the green wire to OUT2
- Connect the red wire to OUT3
- Connect the gray wire to OUT4

## Connecting the controller to the Pi
- The inputs on the L298N are arranged from left to right below output contacts 3 and 4.  Connect them to any of the general-purpose pins on the Raspberry Pi and reference those pins in your code so that they inputs they connect to are arranged in ascending order.  For example:
```
motor = stepper.Motor(7, 11, 13, 15)
```
- Pin 7 should be connected to IN1
- Pin 11 should be connected to IN2
- Pin 13 should be connected to IN3
- Pin 15 should be connected to IN4

## Connecting power and ground
- Connect the positive terminal of the 12 volt power supply to the -12V contact on the controller.
- Connect the ground contact on the controller to both the negative terminal of the power supply **and** to one of the ground pins on the Raspberry Pi.  You may need to use a breadboard.

## More Info
- [Gavin Lyons' notes on using the L298N with a NEMA-11](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/Documentation/Nema11L298N.md)
- [Datasheet for the NEMA-17](https://cdn-shop.adafruit.com/product-files/324/C140-A+datasheet.jpg)
