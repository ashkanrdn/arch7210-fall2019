import matrix
import time
import datetime
import busio
import board

from adafruit_ht16k33.matrix import Matrix8x8x2
i2c = busio.I2C(board.SCL, board.SDA)

gridA = Matrix8x8x2(i2c,address=0x70) 
gridB = Matrix8x8x2(i2c,address=0x74)

happy = matrix.loadImage("/home/pi/arch7210-fall2019/robot/happy.png")
happy.apply(gridB)
happy.rotateRight().apply(gridA)
