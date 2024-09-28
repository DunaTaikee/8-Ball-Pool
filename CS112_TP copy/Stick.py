from cmu_graphics import *
import math
# This class will be the stick that hit the ball

class Stick():

    def __init__(self, pointOnePositionX, pointOnePositionY, pointTwoPositionX, pointTwoPositionY, color):
        # set the defult setting of the stick
        self.length = 250
        self.width = 8
        self.color = color
        self.angle = 0
        self.pointOnePositionX = pointOnePositionX
        self.pointOnePositionY = pointOnePositionY
        self.pointTwoPositionX = pointTwoPositionX
        self.pointTwoPositionY = pointTwoPositionY
        self.isHitting = False
        self.pullingDistance = 0
    
    # def drawStick (self, whiteBall_positionX, whiteBall_positionY):
    #     startPosX = whiteBall_positionX + 50 * math.cos(self.angle)
    #     startPosY = whiteBall_positionY + 50 * math.sin(self.angle)

    #     endPosX = startPosX + self.length * math.cos(self.angle)
    #     endPosY = startPosY + self.length * math.sin(self.angle)
        
    #     return [startPosX, startPosY, endPosX, endPosY]

    
    # Trace the white ball the one head of the stick will always pointing to the stick and rotate with ethe mouse
    # This function will keep update the stick movement with mouse
    def StickRotate(self, whiteBall_positionX, whiteBall_positionY, mouseX, mouseY):
        angle_between = math.atan2(mouseY - whiteBall_positionY, mouseX - whiteBall_positionX)

        # check for the hitting if it does hit the stick will have longer distance to the ball
        if self.isHitting == True:
            extraDistance = min(100, self.pullingDistance * 2)
        else:
            extraDistance = 0

        # twenty is the distance between whiteball and the stick
        startPosX = whiteBall_positionX + (20 + extraDistance) * math.cos(angle_between)
        startPosY = whiteBall_positionY + (20 + extraDistance) * math.sin(angle_between)

        endPosX = startPosX + self.length * math.cos(angle_between)
        endPOsY = startPosY + self.length * math.sin(angle_between)

        # updating the new positions of the stick
        self.pointOnePositionX = startPosX
        self.pointOnePositionY = startPosY

        self.pointTwoPositionX = endPosX
        self.pointTwoPositionY = endPOsY


    # changing the boolean statement of the hitting animation
    def startHitting(self):
        self.isHitting = True
        self.pullingDistance = 0


    # changing the boolean statement of the hitting animation
    def finishHitting(self):
        self.isHitting = False
        self.pullingDistance = 0