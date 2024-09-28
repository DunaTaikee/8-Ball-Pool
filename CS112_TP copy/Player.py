from cmu_graphics import *

# This class is for switching the player of the game

class Player:

    def __init__(self, name):
        self.name = name
        self.isTurn = False
        self.scorePoint = False
        self.isFoul = False

    # Take the turn 
    def Turn_Start(self):
        self.isTurn = True

    # End the turn 
    def Turn_End(self):
        self.isTurn = False

