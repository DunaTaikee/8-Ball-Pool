# This class will make the basic object ball for the whole game
import math

class PoolBall:

    def __init__(self, number, color, positionX, positionY):
        self.size = 15
        self.number = number
        self.color = color
        self.positionX = positionX
        self.positionY = positionY
        self.isPocket = False
        self.isCollision = False
        self.mass = 10
        self.spin = 0
        
        # The velocity will be in vector form for x and y coordinates
        self.X_velocity = 0
        self.Y_velocity = 0
        

    # Method to check for if the ball hit the holes
    def ballMoves(self, changeOfime):
        # Displacement = velocity x ΔT
        self.positionX += self.X_velocity * changeOfime
        self.positionY += self.Y_velocity * changeOfime

     # Find the distance between the ball for collision and for holes for score
    def findDistance(self, Ball):
        x1, y1 = self.positionX, self.positionY
        x2, y2 = Ball.positionX, Ball.positionY
        distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        return distance
    
    # This method will update pool balls positions

    def updateBallPosition(self):

        spin_effect = 0.1  #spin
        if self.spin != 0:
        # the spin will cause the extra acceleration or de-acceleration
            self.X_velocity += self.spin * spin_effect
            self.Y_velocity += self.spin * spin_effect

        # update the position (displacement) base on the velocity
        self.positionX += self.X_velocity
        self.positionY += self.Y_velocity

        # Give the certain value of friction / make sure to slow down
        friction = 0.99  # friction
        self.X_velocity *= friction
        self.Y_velocity *= friction

        # Stop the ball movement when its super small
        if abs(self.X_velocity) < 0.01:
            self.X_velocity = 0
        if abs(self.Y_velocity) < 0.01:
            self.Y_velocity = 0

        # collision of the wall (simply just change the mathematic sign)
        left = self.positionX - self.size
        right = self.positionX + self.size
        top = self.positionY - self.size
        bottom = self.positionY + self.size

        if left <= 235 or right >= 945:
            self.X_velocity *= -1
        if top <= 245 or bottom >= 685:
            self.Y_velocity *= -1
        # (235,245,740,440) coordinate for the inner table
    
# Check the collision between two balls

def checkCollision(ballOne, ballTwo):
    collisionDistance = ballOne.findDistance(ballTwo)
    return collisionDistance <= (ballOne.size + ballTwo.size)


# Achieve the actual calculation of the collison
def collision(ballOne, ballTwo):
    # Because of the in elastic collision, we ll be able to use the conservation of momentum
    Diff_Velocity_x = ballOne.X_velocity - ballTwo.X_velocity
    Diff_Velocity_y = ballOne.Y_velocity - ballTwo.Y_velocity

    # find the displacement
    change_of_X = ballTwo.positionX - ballOne.positionX
    change_of_Y = ballTwo.positionY - ballOne.positionY

    denominator = change_of_X ** 2 + change_of_Y ** 2

    # The ball have to cause collison instead of covering and the denominator cannot be zero
    if  (Diff_Velocity_x * change_of_X + Diff_Velocity_y * change_of_Y >= 0) and (denominator != 0):
        collision_factor = (Diff_Velocity_x * change_of_X + Diff_Velocity_y * change_of_Y) / denominator
        velocity_Final_ballOne_X = ballOne.X_velocity - collision_factor * change_of_X
        velocity_Final_ballOne_Y = ballOne.Y_velocity - collision_factor * change_of_Y
        velocity_Final_ballTwo_X = ballTwo.X_velocity + collision_factor * change_of_X
        velocity_Final_ballTwo_Y = ballTwo.Y_velocity + collision_factor * change_of_Y
    else:
        # if there is no changes / still need to give value to final velocity (but the actual value remian the same)
        velocity_Final_ballOne_X = ballOne.X_velocity
        velocity_Final_ballOne_Y = ballOne.Y_velocity
        velocity_Final_ballTwo_X = ballTwo.X_velocity
        velocity_Final_ballTwo_Y = ballTwo.Y_velocity

    # Giving the calculation velocity of the ball 
    ballOne.X_velocity = velocity_Final_ballOne_X
    ballOne.Y_velocity = velocity_Final_ballOne_Y
    ballTwo.X_velocity = velocity_Final_ballTwo_X
    ballTwo.Y_velocity = velocity_Final_ballTwo_Y

