import pigpio
import time

#Run sudo pigpiod 

class ServoPen:

    def __init__(self):
        self.pi = pigpio.pi()
    
    def apply(self,GPIO_Pin, pulse):
        #0 = off
        #500 = horizontal 
        #1200 = 90 degrees

        self.pi.set_servo_pulsewidth(GPIO_Pin, pulse)
        time.sleep(1)
        
    def up(self):
        self.apply(18,1200)
    
    def down(self):
        self.apply(18,500)
