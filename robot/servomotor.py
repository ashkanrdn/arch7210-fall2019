import pigpio
import time

#Run sudo pigpiod 

class ServoPen:

    def __init__(self):
        self.pi = pigpio.pi()
    
    def apply(self,GPIO_Pin, pulse):
        #0 = off
        #1000 = position anti-clockwise
        #1500 = middle
        #2000 = position clockwise

        self.pi.set_servo_pulsewidth(GPIO_Pin, pulse)
        time.sleep(1)
