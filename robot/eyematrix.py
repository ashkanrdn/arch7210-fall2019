import matrix
import time
import datetime
import busio
import board

from adafruit_ht16k33.matrix import Matrix8x8x2
i2c = busio.I2C(board.SCL, board.SDA)

gridA = Matrix8x8x2(i2c,address=0x70,auto_write = False) 
gridB = Matrix8x8x2(i2c,address=0x74,auto_write = False)

normal_center = matrix.loadImage("/home/pi/arch7210-fall2019/robot/eyes/normal_center.png")
normal_left = matrix.loadImage("/home/pi/arch7210-fall2019/robot/eyes/normal_left.png")
normal_right = matrix.loadImage("/home/pi/arch7210-fall2019/robot/eyes/normal_right.png")

while True:

    normal_center.apply(gridB)
    normal_center.apply(gridA)
    time.sleep(0.5)
    
    normal_left.apply(gridA)
    normal_left.apply(gridB)
    time.sleep(0.5)
    
    normal_center.apply(gridB)
    normal_center.apply(gridA)
    time.sleep(0.5)
    
    
    normal_right.apply(gridA)
    normal_right.apply(gridB)
    time.sleep(0.5)
#happy.rotateRight().apply(gridA)




