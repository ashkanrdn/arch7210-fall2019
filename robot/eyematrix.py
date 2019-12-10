import matrix
import busio
import board

from adafruit_ht16k33.matrix import Matrix8x8x2
i2c = busio.I2C(board.SCL, board.SDA)

HAPPY_CENTER = matrix.loadImage("/home/pi/arch7210-fall2019/robot/eyes/happy_center.png")
HAPPY_CORNER = matrix.loadImage("/home/pi/arch7210-fall2019/robot/eyes/happy_left.png")
NORMAL_CENTER = matrix.loadImage("/home/pi/arch7210-fall2019/robot/eyes/normal_center.png")
NORMAL_LEFT = matrix.loadImage("/home/pi/arch7210-fall2019/robot/eyes/normal_left.png")
ANGRY_CENTER = matrix.loadImage("/home/pi/arch7210-fall2019/robot/eyes/angry_center.png")

class RobotEyes:
    
    def __init__(self):
        self.leftEye = Matrix8x8x2(i2c,address=0x70,auto_write = False) 
        self.rightEye = Matrix8x8x2(i2c,address=0x74,auto_write = False)  

    def applyLeft(self, image):
        """Apply image to just the left eye"""
        image.rotateLeft().apply(self.leftEye)
        
    def applyRight(self, image):
        """Apply image to just the right eye"""
        image.rotateRight().apply(self.rightEye)
        
    def applyBoth(self, image):
        """Apply image to both eyes"""
        self.applyLeft(image)
        self.applyRight(image)
        
    def applyMirrored(self, image):
        """Apply mirrored image to both eyes"""
        self.applyRight(image)
        self.applyLeft(image.flip())
        
    def happy_center(self):
        """Generate happy eyes in center of matrix"""
        self.applyMirrored(HAPPY_CENTER)
        
    def happy_left(self):
        """Generate happy eyes in left of matrix"""
        self.applyBoth(HAPPY_CORNER.flip())
        
    def happy_right(self):
        """Generate happy eyes in right of matrix"""
        self.applyBoth(HAPPY_CORNER)

    def normal_center(self):
        """Generate normal eyes in center of matrix"""
        self.applyBoth(NORMAL_CENTER)
        
    def normal_left(self):
        """Generate normal eyes in left of matrix"""
        self.applyBoth(NORMAL_LEFT.flip())
        
    def normal_right(self):
        """Generate normal eyes in right of matrix"""
        self.applyBoth(NORMAL_LEFT)
    
    def angry_center(self):
        self.applyLeft(ANGRY_CENTER.flip())
        self.applyRight(ANGRY_CENTER)
        
eyes = RobotEyes()
eyes.angry_center()

"""

normal_left = matrix.loadImage("/home/pi/arch7210-fall2019/robot/eyes/normal_left.png")
normal_right = matrix.loadImage("/home/pi/arch7210-fall2019/robot/eyes/normal_right.png")
angry_right = matrix.loadImage("/home/pi/arch7210-fall2019/robot/eyes/angry_center.png")


angry_right.apply(rightEye)
angry_left = angry_right.flip()

angry_left.apply(leftEye)
"""
