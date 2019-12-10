import matrix
import busio
import board
import time
from adafruit_ht16k33.matrix import Matrix8x8x2
i2c = busio.I2C(board.SCL, board.SDA)

"""Links to all the images used for the eyes"""

HAPPY_CENTER = matrix.loadImage("/home/pi/arch7210-fall2019/robot/eyes/happy_center.png")
HAPPY_CORNER = matrix.loadImage("/home/pi/arch7210-fall2019/robot/eyes/happy_left.png")
NORMAL_CENTER = matrix.loadImage("/home/pi/arch7210-fall2019/robot/eyes/normal_center.png")
NORMAL_LEFT = matrix.loadImage("/home/pi/arch7210-fall2019/robot/eyes/normal_left.png")
NORMAL_CORNER = matrix.loadImage("/home/pi/arch7210-fall2019/robot/eyes/normal_corner.png")
NORMAL_TOP = matrix.loadImage("/home/pi/arch7210-fall2019/robot/eyes/normal_up.png")
ANGRY_CENTER = matrix.loadImage("/home/pi/arch7210-fall2019/robot/eyes/angry_center.png")
ANGRY_LEFT = matrix.loadImage("/home/pi/arch7210-fall2019/robot/eyes/angry_left.png")
ANGRY_RIGHT = matrix.loadImage("/home/pi/arch7210-fall2019/robot/eyes/angry_right.png")
BLINK_HALFOPEN = matrix.loadImage("/home/pi/arch7210-fall2019/robot/eyes/blink_halfway_open.png")
BLINK_HALFCLOSED = matrix.loadImage("/home/pi/arch7210-fall2019/robot/eyes/blink_halfway_closed.png")
BLINK_CLOSED = matrix.loadImage("/home/pi/arch7210-fall2019/robot/eyes/blink_closed.png")
TIRED = matrix.loadImage("/home/pi/arch7210-fall2019/robot/eyes/tired_center.png")
SAD_CENTER = matrix.loadImage("/home/pi/arch7210-fall2019/robot/eyes/sad_center.png")
SAD_LEFT = matrix.loadImage("/home/pi/arch7210-fall2019/robot/eyes/sad_left.png")
SAD_RIGHT = matrix.loadImage("/home/pi/arch7210-fall2019/robot/eyes/sad_right.png")


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

    """=============HAPPY EYES============="""
        
    def happy_center(self):
        """Generate happy eyes in center of matrix"""
        self.applyMirrored(HAPPY_CENTER)
        
    def happy_left(self):
        """Generate happy eyes in left of matrix"""
        self.applyBoth(HAPPY_CORNER.flip())
        
    def happy_right(self):
        """Generate happy eyes in right of matrix"""
        self.applyBoth(HAPPY_CORNER)
        
    """=============NORMAL EYES============="""

    def normal_center(self):
        """Generate normal eyes in center of matrix"""
        self.applyBoth(NORMAL_CENTER)
        
    def normal_left(self):
        """Generate normal eyes in left of matrix"""
        self.applyBoth(NORMAL_LEFT.flip())
        
    def normal_right(self):
        """Generate normal eyes in right of matrix"""
        self.applyBoth(NORMAL_LEFT)
        
    def normal_up(self):
        """Generate normal eyes in top center of matrix"""
        self.applyBoth(NORMAL_TOP)
        
    def normal_down(self):
        """Generate normal eyes in bottom center of matrix"""
        self.applyBoth(NORMAL_TOP.flop())

    def normal_down_left(self):
        """Generate normal eyes in left bottom corner of matrix"""
        self.applyBoth(NORMAL_CORNER)
        
    def normal_down_right(self):
        """Generate normal eyes in right bottom corner of matrix"""
        self.applyBoth(NORMAL_CORNER.flip())
        
    def normal_up_left(self):
        """Generate normal eyes in left upper corner of matrix"""
        self.applyBoth(NORMAL_CORNER.flop())

    def normal_up_right(self):
        """Generate normal eyes in right upper corner of matrix"""
        self.applyBoth(NORMAL_CORNER.transpose())
        
    """=============ANGRY EYES============="""
    
    def angry_center(self):
        """Generate angry eyes in center of matrix"""
        self.applyMirrored(ANGRY_CENTER)
        
    def angry_right(self):
        """Generate angry eyes in right of matrix"""
        self.applyLeft(ANGRY_RIGHT)
        self.applyRight(ANGRY_LEFT)
        
    def angry_left(self):
        """Generate angry eyes in left of matrix"""
        self.applyLeft(ANGRY_LEFT.flip())
        self.applyRight(ANGRY_RIGHT.flip())
        
    """=============TIRED EYES============="""
    
    def tired_eyes(self):
        """Generate tired eyes in the center of matrix"""
        self.applyBoth(TIRED)
        
    """=============SAD EYES============="""

    def sad_center(self):
        """Generate sad eyes in the center of matrix"""
        self.applyMirrored(SAD_CENTER)
        
    def sad_left(self):
        """Generate sad eyes in the left of matrix"""
        self.applyLeft(SAD_LEFT.flip())
        self.applyRight(SAD_RIGHT.flip())
        
    def sad_right(self):
        """Generate sad eyes in the right of matrix"""
        self.applyLeft(SAD_RIGHT)
        self.applyRight(SAD_LEFT)
        
    """=============BLINK EYES============="""
    
    def halfway_open(self):
        """Eyes closed 3/4 of the way"""
        self.applyBoth(BLINK_HALFOPEN)
        
    def halfway_closed(self):
        """Eyes closed 1/2 of the way"""
        self.applyBoth(BLINK_HALFCLOSED)
        
    def closed(self):
        """Eyes closed"""
        self.applyBoth(BLINK_CLOSED)
        
    """=============ANIMATIONS============="""
    
    def animate(self, actions, duration):
        """List of actions and time duration for each eyes transition"""
        actions[0]()
        sleepTime = duration / (len(actions) - 1)
        
        for action in actions[1:]:
            time.sleep(sleepTime)
            action()
    
    def blink(self, duration=0.25):
        """Eyes blink"""
        self.animate([
            self.normal_center,
            self.halfway_open,
            self.halfway_closed,
            self.closed,
            self.halfway_closed,
            self.halfway_open,
            self.normal_center
        ], duration)

    def bored(self, duration = 1.2):
        """Rolling eyes"""
        self.animate([
            self.normal_center,
            self.normal_left,
            self.normal_up_left,
            self.normal_up,
            self.normal_up_right,
            self.normal_right,
            self.normal_center
        ], duration)
        
    def tired(self,duration = 1):
        """Eyes clossing and changing to yellow"""
        self.animate([
            self.normal_center,
            self.halfway_open,
            self.halfway_closed,
            self.closed,
            self.tired_eyes
        ], duration)

    def wander_left_right(self, duration = 1):
        """Eyes moving left and right"""
        self.animate([
            self.normal_center,
            self.normal_left,
            self.normal_center,
            self.normal_right,
            self.normal_center,
        ], duration)
        
    def wander_around(self, duration = 1):
        """Eyes moving in an diagonal pattern"""
        self.animate([
            self.normal_center,
            self.normal_up_left,
            self.normal_up,
            self.normal_up_right,
            self.normal_center,
            self.normal_down_left,
            self.normal_down,
            self.normal_down_right,
            self.normal_center
        ], duration)
        
    def angry(self, duration = 1):
        self.animate([
            self.angry_center,
            self.angry_left,
            self.angry_center,
            self.angry_right,
            self.angry_center
        ], duration)
        
    def sad(self, duration = 1):
        self.animate([
            self.sad_center,
            self.sad_right,
            self.sad_center,
            self.sad_left,
            self.sad_center,
        ], duration)
        

#Lines just for testing                
#eyes = RobotEyes()
#eyes.sad()
