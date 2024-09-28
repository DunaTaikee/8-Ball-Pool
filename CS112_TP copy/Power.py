from Stick import *

# This class is for showing the power of the hitting

class Power:
    def __init__(self):
        self.coordinateX = 1085
        self.coordinateY = 220
        self.length = 100
        self.height = 10
        self.currentPower = 1
        self.color = 'white'
        self.powerWidth = 1

    # update the current power with the pullingDistance in Stick class
    def updatePower(self, pullingDistance):
        self.currentPower = min(pullingDistance * 2, self.length)
        self.powerWidth = self.currentPower
