# All the import values
from cmu_graphics import *
import math
from PoolBall import *
from Stick import *
from Power import *
from Player import *

# This file will be the play control of the game (including gaming setting and every UI)

def onAppStart(app):
    reset(app)


# The default setting for every app variables
def reset(app):
    # app for UI as changing of pages
    app.width = 1200
    app.height = 800
    app.home = True
    app.countForSpace = 0 # This means the space key will only work for onece in the intro page
    app.selectModePage = False
    app.infoPage = False
    app.tutorialPage = False
    app.select_challengePage = False
    app.select_playerPage = False
    app.challengeMode = None
    app.challenge_gamePlayPage = False
    app.challengeFail = False
    app.multi_gamePlayPage = False
    app.startTheGame = False
    app.gameOver = False
    app.playerOneIsWinner = False
    app.playerTwoIsWinner = False
    app.easyChallengeFinish = False
    app.hardChallengeFinish = False
    # app.stepsPerSecond = 60
    app.stepsPerSecond = 120
    app.time = 300
    app.counter = 0
    app.hitTimes = 0
    app.needTurnCheck = False
    app.needWhiteBallCheck = False
    app.firstCollisionBall = None
    app.allPocket = []
    app.isScore = False
    app.randomPut = True

    # Need the score the record for the playerOne and playerTWo
    app.score_P1 = 0
    app.score_P2 = 0

    # The mouse coordinates
    app.mouseX = 0
    app.mouseY = 0

    # Creating 15 pool balls base on the ball class by hardcoding
    app.balls_coordinates = arrange_balls([])

    app.whiteBall = PoolBall(0, 'white', 400, 460)
    app.blackBall = PoolBall(8, 'black', app.balls_coordinates[7][0], app.balls_coordinates[7][1])
    
    # The 1 - 7 is yellow which will represent solid
    app.ballOne = PoolBall(1, 'yellow', app.balls_coordinates[0][0], app.balls_coordinates[0][1])
    app.ballTwo = PoolBall(2, 'yellow', app.balls_coordinates[1][0], app.balls_coordinates[1][1])
    app.ballThree = PoolBall(3, 'yellow', app.balls_coordinates[2][0], app.balls_coordinates[2][1])
    app.ballFour = PoolBall(4, 'yellow', app.balls_coordinates[3][0], app.balls_coordinates[3][1])
    app.ballFive = PoolBall(5, 'yellow', app.balls_coordinates[4][0], app.balls_coordinates[4][1])
    app.ballSix = PoolBall(6, 'yellow', app.balls_coordinates[5][0], app.balls_coordinates[5][1])
    app.ballSeven = PoolBall(7, 'yellow', app.balls_coordinates[6][0], app.balls_coordinates[6][1])

    # The 9 - 15 is red which will represent strip
    app.ballNine = PoolBall(9, 'red', app.balls_coordinates[8][0], app.balls_coordinates[8][1])
    app.ballTen = PoolBall(10, 'red', app.balls_coordinates[9][0], app.balls_coordinates[9][1])
    app.ballEleven = PoolBall(11, 'red', app.balls_coordinates[10][0], app.balls_coordinates[10][1])
    app.ballTwelve = PoolBall(12, 'red', app.balls_coordinates[11][0], app.balls_coordinates[11][1])
    app.ballThirteen = PoolBall(13, 'red', app.balls_coordinates[12][0], app.balls_coordinates[12][1])
    app.ballFourteen = PoolBall(14, 'red', app.balls_coordinates[13][0], app.balls_coordinates[13][1])
    app.ballFivteen = PoolBall(15, 'red', app.balls_coordinates[14][0], app.balls_coordinates[14][1])

    app.allBalls = [app.whiteBall, app.blackBall, app.ballOne, app.ballTwo, app.ballThree, app.ballFour, 
                 app.ballFive, app.ballSix, app.ballSeven, app.ballNine, app.ballTen, app.ballEleven, app.ballTwelve,
                 app.ballTwelve, app.ballThirteen, app.ballFourteen, app.ballFivteen]
    
    # a list for all solids and a list for all stripes
    app.allSolid = [app.ballOne, app.ballTwo, app.ballThree, app.ballFour, app.ballFive, app.ballSix, app.ballSeven]

    app.allStrip = [app.ballNine, app.ballTen, app.ballEleven, app.ballTwelve, app.ballThirteen, app.ballThirteen, app.ballFourteen, app.ballFivteen]

    # a list of balls for easy challenge
    app.easyChallenge = [app.whiteBall, app.ballOne, app.ballThree, app.ballFive]

    # a list of coordinates to check for the ball inside the pocket
    app.holeCoordinates = [(225,240), (985,240), (225,690), (985,690), (605,225), (605,705)]
    app.distance = 0

    # create a stick object
    app.Stick = Stick(0, 0, 0, 0, 'brown')

    # create a power object
    app.Power = Power()

    # create two players
    app.PlayerOne = Player('Player One')
    app.PlayerTwo = Player('Player Two')

    app.currentPlayer = app.PlayerOne


# The drawing 
# Only the intro page I cited online, every other UI and image I draw it on my IPad
def redrawAll(app):
    # The intro page
    if app.home == True:
        drawImage('intro.jpg', 600, 400, align = 'center', width = 1200, height = 800)
        # Citation (From this link): https://www.artstation.com/artwork/d08e3x
        drawLabel('Press SPACE to Start the Game!', 900, 650, font = 'montserrat', fill = 'white', size = 20, bold = True, italic = True)
    
    elif app.infoPage == True:
        drawImage('info.jpg', 600, 400, align='center', width = 1200, height = 800)
        # The coordinates of the back button
        drawLabel('My contact information:', 600, 200, align='center', fill = 'black', size = 30, bold = True, italic = True)
        drawLabel('Name: Tait Duan', 600, 240, align='center', fill = 'black', size = 30, bold = True, italic = True)
        drawLabel('Email: siruid@andrew.cmu.edu', 600, 280, align='center', fill = 'black', size = 30, bold = True, italic = True)
        drawLabel('Phone: 434-466-0443', 600, 320, align='center', fill = 'black', size = 30, bold = True, italic = True)

        drawLabel('SciP:', 420, 380, align='left', fill = 'black', size = 30, bold = True, italic = True)
        drawLabel('The main physics engine involved:', 420, 420, align='left', fill = 'black', size = 30, bold = True, italic = True)
        drawLabel('momentum / collision / friction', 420, 460, align='left', fill = 'black', size = 30, bold = True, italic = True)

        drawLabel('Press and hold the A button to hit the white ball', 300, 580, align='left', fill = 'maroon', size = 30, bold = True, italic = True)
        drawLabel('Wait for all balls to stop,', 300, 620, align='left', fill = 'maroon', size = 30, bold = True, italic = True)
        drawLabel('The stick appears before the next shot is taken', 300, 660, align='left', fill = 'maroon', size = 30, bold = True, italic = True)


        drawRect(1075,27,100,100,fill = 'purple', opacity = 0)

    elif app.playerOneIsWinner  == True:
        drawImage('winner1.jpg', 600, 400, align='center', width = 1200, height = 800)
    
    elif app.playerTwoIsWinner == True:
        drawImage('winner2.jpg', 600, 400, align='center', width = 1200, height = 800)

    # The select mode page
    elif app.selectModePage == True:
        drawImage('select_mode.jpg', 600, 400, align='center', width = 1200, height = 800)
        # The coordinates of the home button
        drawRect(25,30,100,100,fill = 'purple', opacity = 0)
        # The coordinates of the info button
        drawRect(140,30,100,100,fill = 'purple', opacity = 0)
        # The coordinates of three modes
        for i in range(3):
            drawRect(380, 80 + i * 200 + i * 20, 450, 200, fill = 'purple', opacity = 0)

    # The tutorial page
    elif app.tutorialPage == True:
        drawImage('tutorial.jpg', 600, 400, align='center', width = 1200, height = 800) 
        drawLabel('Goal: Pocket all your balls (stripes or solids) then the 8-ball.', 230, 300, size = 20, align = 'left', bold = True)
        drawLabel('Setup: Balls in a triangle; 8-ball in the center; apex ball on foot spot.', 230, 340, size = 20, align = 'left', bold = True)
        drawLabel('Break Shot: Must pocket a ball or hit four balls to rails.', 230, 380, size = 20, align = 'left', bold = True)
        drawLabel('Open Table: Choose stripes or solids after the break based on first pocketed ball.', 230, 420, size = 20, align = 'left', bold = True)
        drawLabel('Turns: Continue shooting if you legally pocket a ball.', 230, 460, size = 20, align = 'left', bold = True)
        drawLabel('Legal Shot: Hit your group of balls first and pocket a ball or hit a rail.', 230, 500, size = 20, align = 'left', bold = True)
        drawLabel('Fouls: Includes scratching, wrong ball first, no ball hit, cue ball off table.', 230, 540, size = 20, align = 'left', bold = True)
        drawLabel('Cue Ball in Hand: Place cue ball anywhere for next shot after an opponents foul.', 230, 580, size = 20, align = 'left', bold = True)
        drawLabel('Pocketing the 8-Ball: Win by legally pocketing the 8-ball after clearing your balls.', 230, 620, size = 20, align = 'left', bold = True)
        drawLabel('Losing the Game: Lose by pocketing 8-ball early, on a foul, or in the wrong pocket.', 230, 660, size = 20, align = 'left', bold = True)

    # The select level of challenge page
    elif app.select_challengePage == True:
        drawImage('select_challenge.jpg', 600, 400, align='center', width = 1200, height = 800)
        # The coordinates of the two level button
        drawRect(345,250,505,150,fill = 'purple', opacity = 0)
        drawRect(345,450,505,150,fill = 'purple', opacity = 0)

    # The select player mode page
    elif app.select_playerPage == True:
        drawImage('select_player.jpg', 600, 400, align='center', width = 1200, height = 800) 
        drawRect(500,35,230,230,fill = 'purple', opacity = 0)

    elif app.challengeFail == True:
        drawImage('challengeFail.jpg', 600, 400, align='center', width = 1200, height = 800) 
    
    # The challenge game play page
    elif app.challenge_gamePlayPage == True:
        drawImage('challenge_gamePlay.jpg', 600, 400, align='center', width = 1200, height = 800)
        # if app.startTheGame == False:
        # gameplay(app)
        challenge(app)
        # drawCircle(200, 200, 10, fill = 'yellow')

        # The coordinates of the six ball holes
        drawCircle(225,240,30,fill = 'red', opacity = 0)
        drawCircle(985,240,30,fill = 'red', opacity = 0)

        drawCircle(225,690,30,fill = 'red', opacity = 0)
        drawCircle(985,690,30,fill = 'red', opacity = 0)

        drawCircle(605,225,30,fill = 'red', opacity = 0)
        drawCircle(605,705,30,fill = 'red', opacity = 0)

        # The coordinates of the whole pool table
        # The outer rect of the pool table
        drawRect(600,475,800,550,fill = 'pink', align = 'center', opacity = 0)   
        # The inner rect of the pool table (for collision on the wall) 
        # I will use this coordinates to test if it hits the way with the collision
        drawRect(235,245,740,440,fill = 'purple', opacity = 0) 
        drawLabel(app.time, 1135, 170, fill = 'maroon', size = 40, bold = True)
    
    elif app.easyChallengeFinish == True:
        drawImage('easyChallengeFinish.jpg', 600, 400, align='center', width = 1200, height = 800)
    
    elif app.hardChallengeFinish == True:
        drawImage('hardChallengeFinish.jpg', 600, 400, align='center', width = 1200, height = 800)

    # The multi-player game play page
    elif app.multi_gamePlayPage == True:
        drawImage('multi_gamePlay.jpg', 600, 400, align='center', width = 1200, height = 800)
        gameplay(app)
        scoreShow(app)

        # The coordinates of the pool table and the holes will have some small difference in number
        drawCircle(225,240,25,fill = 'red', opacity = 0)
        drawCircle(985,240,25,fill = 'red', opacity = 0)

        drawCircle(225,690,25,fill = 'red', opacity = 0)
        drawCircle(985,690,25,fill = 'red', opacity = 0)

        drawCircle(605,225,20,fill = 'red', opacity = 0)
        drawCircle(605,705,20,fill = 'red', opacity = 0)

        # The coordinates of the whole pool table
        # The outer rect of the pool table
        # drawRect(600,475,800,550,fill = 'pink', align = 'center', opacity = 20)   
        # The inner rect of the pool table (for collision on the wall) 
        # I will use this coordinates to test if it hits the way with the collision
        # drawRect(235,245,740,440,fill = 'purple', opacity = 50) 
        drawLabel(f'''It's {app.currentPlayer.name}'s turn''', 600, 90, fill = 'black', size = 50, bold = True)
    
  
# The ball settelements  
def arrange_balls(balls_coordinates):
    startX = 900
    startY = 400
    space = 0
    rows = 5
    size = 15
    for col in range(5):
        for row in range(rows):
            positionX = startX - (col * size * 2 + space * col)
            positionY = (startY + size * col) + row * (size * 2)
            ball_coordinates = [positionX, positionY]
            balls_coordinates.append(ball_coordinates)
        rows -= 1
    return balls_coordinates


# This is the foixed version of checkCollison function in Ball class 
# (This will check every possible collision instead of targed two balls)
def checkCollisonAll(app):
    num = len(app.allBalls)
    for i in range(num):
        for j in range(i + 1, num):
            ballOne = app.allBalls[i]
            ballTwo = app.allBalls[j]
            change_of_x = ballOne.positionX - ballTwo.positionX  # Its basicly delta x
            change_of_y = ballOne.positionY - ballTwo.positionY  # Its basicly delta y
            distance = math.sqrt(change_of_x ** 2 + change_of_y ** 2)
            if distance <= ballOne.size + ballTwo.size: # The distance smaller than sum of size means collison

                collision(ballOne, ballTwo)


# check collision for challenge game
def checkCollisonChallenge(app):
    num = len(app.easyChallenge)
    for i in range(num):
        for j in range(i + 1, num):
            ballOne = app.easyChallenge[i]
            ballTwo = app.easyChallenge[j]
            change_of_x = ballOne.positionX - ballTwo.positionX  # Its basicly delta x
            change_of_y = ballOne.positionY - ballTwo.positionY  # Its basicly delta y
            distance = math.sqrt(change_of_x ** 2 + change_of_y ** 2)
            if distance <= ballOne.size + ballTwo.size: # The distance smaller than sum of size means collison
                collision(ballOne, ballTwo)


# Need a function to check what the white ball hit first

def whiteBallCollison(app):
    num = len(app.allBalls)
    for i in range(1, num):
        distance = app.whiteBall.findDistance(app.allBalls[i])
        if (distance <= app.whiteBall.size + app.allBalls[i].size) and (app.firstCollisionBall == None):
            app.firstCollisionBall = app.allBalls[i].color
            break


# To start the setting of the game
def gameplay(app):
    for ball in app.allBalls:
        if ball.isPocket == False:
            drawCircle(ball.positionX, ball.positionY, ball.size, fill = ball.color, border = 'black')
        elif ball.isPocket == True:
            drawCircle(0, 0, ball.size, fill = ball.color, border = 'black', opacity = 50)

    
    if (checkStop(app)) and (app.whiteBall.isPocket == False):
        drawLine(app.Stick.pointOnePositionX, app.Stick.pointOnePositionY, app.Stick.pointTwoPositionX, app.Stick.pointTwoPositionY, fill = 'brown', lineWidth = app.Stick.width)

    if app.multi_gamePlayPage == True:
        drawRect(1085, 100, app.Power.length, app.Power.height, fill = app.Power.color)
        drawRect(1085, 100, app.Power.currentPower, app.Power.height, fill = 'green')
    else:
        drawRect(app.Power.coordinateX, app.Power.coordinateY, app.Power.length, app.Power.height, fill = app.Power.color)
        drawRect(app.Power.coordinateX, app.Power.coordinateY, app.Power.currentPower, app.Power.height, fill = 'green')


# To show the score on the side line
def scoreShow(app):

    num_solid = 7
    num_strip = 7

    # The solid side
    for i in range(len(app.allSolid)):
        if app.allSolid[i].isPocket == True:
            num_solid -= 1
    
    for j in range(num_solid):
        drawCircle(120, 300 + j * 50, 15, fill = 'yellow', border = 'black')

    # The strip side
    for x in range(len(app.allStrip)):
        if app.allStrip[x].isPocket == True:
            num_strip -= 1
    
    for y in range(num_strip):
        drawCircle(1085, 300 + y * 50, 15, fill = 'red', border = 'black')


# To start the setting of the challenge
def challenge(app):
    for ball in app.easyChallenge:
        if ball.isPocket == False:
            drawCircle(ball.positionX, ball.positionY, ball.size, fill = ball.color, border = 'black')

    if (app.whiteBall.X_velocity == 0) and (app.whiteBall.X_velocity == 0) and (app.whiteBall.isPocket == False):
        drawLine(app.Stick.pointOnePositionX, app.Stick.pointOnePositionY, app.Stick.pointTwoPositionX, app.Stick.pointTwoPositionY, fill = 'brown', lineWidth = app.Stick.width)
    
    drawRect(app.Power.coordinateX, app.Power.coordinateY, app.Power.length, app.Power.height, fill = app.Power.color)
    drawRect(app.Power.coordinateX, app.Power.coordinateY, app.Power.currentPower, app.Power.height, fill = 'green')


# The mouse movement
def onMousePress(app, mouseX, mouseY):

    # The home button and info button checking
    if app.home == False and app.infoPage == False and 25 <= mouseX <= 125 and 30 <= mouseY <= 135:
        reset(app)
    
    elif app.home == False and app.infoPage == False and 140 <= mouseX <= 240 and 30 <= mouseY <= 135:
        # print(app.infoPage)
        app.infoPage = True

    # The back button checking
    elif app.infoPage == True and 1075 <= mouseX <= 1175 and 27 <= mouseY <= 127:
        app.infoPage = False
    
    # The three modes button checking
    elif app.selectModePage == True and 380 <= mouseX <= 830 and 80 <= mouseY <= 280:
        app.tutorialPage = True
        app.selectModePage = False

    elif app.selectModePage == True and 380 <= mouseX <= 830 and 300 <= mouseY <= 500:
        app.select_challengePage = True
        app.selectModePage = False

    elif app.selectModePage == True and 380 <= mouseX <= 830 and 520 <= mouseY <= 700:
        app.select_playerPage = True
        app.selectModePage = False
    
    # The two challenge level button checking
    elif app.select_challengePage  == True and 345 <= mouseX <= 850 and 250 <= mouseY <= 400:
        app.select_challengePage = False
        app.challengeMode = 'Easy'
        # print(app.challengeMode)
        app.challenge_gamePlayPage = True
    
    elif app.select_challengePage  == True and 345 <= mouseX <= 850 and 450 <= mouseY <= 700:
        app.select_challengePage = False
        app.challengeMode = 'Hard'
        # print(app.challengeMode)
        app.challenge_gamePlayPage = True

    # The start button checking for select player page
    elif app.select_playerPage  == True and 500 <= mouseX <= 730 and 35 <= mouseY <= 265:
        app.select_playerPage = False
        app.multi_gamePlayPage = True
    
    elif app.challenge_gamePlayPage == True:
        app.startTheGame = True
        if (app.whiteBall.isPocket == True) and (235 <= mouseX <= 945) and (245 <= mouseY <= 685):
            app.whiteBall.positionX, app.whiteBall.positionY = 400, 460
            app.whiteBall.isPocket = False
            if app.challengeMode == 'Easy':
                app.time -= 50
            elif app.challengeMode == 'Hard':
                app.time -= 100

        # (235,245,740,440) 
    elif app.multi_gamePlayPage == True:
        if (app.whiteBall.isPocket == True) and (235 <= mouseX <= 945) and (245 <= mouseY <= 685):
            app.whiteBall.positionX, app.whiteBall.positionY = mouseX, mouseY
            app.whiteBall.isPocket = False

        elif (checkIfFouled(app) == True) and (235 <= mouseX <= 945) and (245 <= mouseY <= 685):
            app.whiteBall.positionX, app.whiteBall.positionY = mouseX, mouseY
            app.whiteBall.isPocket = False

    # I might change the version of controling stick by mouse prese and mouse release


def findDistance(x1, x2, Ball):
        x1, y1 = x1, x2
        x2, y2 = Ball.positionX, Ball.positionY
        distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        return distance


# The mouse movements
def onMouseMove(app, mouseX, mouseY):
    app.mouseX = mouseX
    # print(app.mouseX)
    app.mouseY = mouseY
    # print(app.mouseY)


def checkPocket(app):
    for ball in app.allBalls:
        for x1, x2 in app.holeCoordinates:
            distance = findDistance(x1, x2, ball)
            if (distance <= ball.size + 30) and (ball.isPocket == False):
                # print('############### SCORE ###############')
                ball.isPocket = True
                ball.X_velocity = 0
                ball.Y_velocity = 0
                app.allPocket.append(ball)

                app.isScore = True
    # print(app.allPocket)

def checkPocket_Challenge(app):
    for ball in app.easyChallenge:
        for x1, x2 in app.holeCoordinates:
            distance = findDistance(x1, x2, ball)
            if (distance <= ball.size + 30) and (ball.isPocket == False):
                # print('is score')
                ball.isPocket = True
                ball.X_velocity = 0
                ball.Y_velocity = 0
    # print(app.allPocket)



# This function will check are all the balls velocity is zero (which means they all stop)
def checkStop(app):
    for ball in app.allBalls:
        if (ball.X_velocity != 0) or (ball.Y_velocity != 0):
            return False
    return True

# From the logic module this function will be able to check who is the winner

def finishAllSolid(app):
    for ball in app.allSolid:
        if ball.isPocket != True:
            return False
    return True

def finishAllStrip(app):
    for ball in app.allStrip:
        if ball.isPocket != True:
            app.playerOneIsWinner = False
            return False
    return True
        
# def checkWinners_1(app):
#     for ball in app.allSolid:
#         if ball.isPocket != True:
#             app.playerOneIsWinner = False
#             return 
#     app.playerOneIsWinner = True
#     return 

def checkWinners_1(app):
    if(finishAllSolid(app) == True) and (app.blackBall.isPocket == True):
        app.playerOneIsWinner = True

# def checkWinners_2(app):
#     for ball in app.allStrip:
#         if ball.isPocket != True:
#             app.playerTwoIsWinner = False
#             return 
#     app.playerTwoIsWinner = True
#     return 

def checkWinners_2(app):
    if(finishAllStrip(app) == True) and (app.blackBall.isPocket == True):
        app.playerTwoIsWinner = True

def checkChallenge(app):
    if app.challengeMode == 'Easy':
        for ball in app.easyChallenge:
            if ball.isPocket != True:
                app.easyChallengeFinish = False
                return 
        app.easyChallengeFinish = True
        return 
    
    elif app.challengeMode == 'Hard':
        for ball in app.easyChallenge:
            if ball.isPocket != True:
                app.hardChallengeFinish = False
                return 
        app.hardChallengeFinish = True
        return 


# The key movements
def onKeyPress(app, key):
    # For move on from the intro page
    if key == 'space' and app.countForSpace == 0:
        app.countForSpace += 1
        app.home = False
        app.selectModePage = True
    
    if (checkStop(app) == True):
        if key == 'a' and (app.challenge_gamePlayPage == True or app.multi_gamePlayPage == True) and (app.whiteBall.isPocket == False):
            # app.whiteBall.spin = 0
            app.Stick.startHitting()


        # app.white_ball.velocityX = 5
        # app.white_ball.velocityY = 5

    # if (checkStop(app) == True):
    #     if key == 't' and (app.challenge_gamePlayPage == True or app.multi_gamePlayPage == True) and (app.whiteBall.isPocket == False):
    #         print('Top Spin')
    #         app.whiteBall.spin = 1
    #     elif key == 'b' and (app.challenge_gamePlayPage == True or app.multi_gamePlayPage == True) and (app.whiteBall.isPocket == False):
    #         print('Bottom Spin')
    #         app.whiteBall.spin = -1
    
    if key == 'n' and app.multi_gamePlayPage == True:
        # print('n')
        cheatSolid(app)
    
    if key == 'm' and app.multi_gamePlayPage == True:
        # print('m')
        cheatStrip(app)


# The potential code for finding the spin
def findSpin(angle, hitPower):
    spin_C = angle / 90.0  # Trying to figure out the angle and power relate to the spin
    spinPower = spin_C * hitPower
    return spinPower


def onKeyRelease(app, key):

    if (checkStop(app) == True):
        if key == 'a' and (app.challenge_gamePlayPage == True or app.multi_gamePlayPage == True) and (app.whiteBall.isPocket == False):
            app.Stick.finishHitting()
            angle_between = math.atan2(app.mouseY - app.whiteBall.positionY, app.mouseX - app.whiteBall.positionX)
            power = app.Power.currentPower / 5   # This means the max will be 20
            app.Power.currentPower = 1

            # spinPower = findSpin(angle_between, power)
            # app.whiteBall.spin = spinPower
            
            # updating white balls speed
            app.whiteBall.X_velocity = power * math.cos(angle_between + math.pi)
            app.whiteBall.Y_velocity = power * math.sin(angle_between + math.pi)

            app.hitTimes += 1
            # print(app.hitTimes)
            app.needTurnCheck = True
            app.firstCollisionBall = None
            app.allPocket = []
            app.isScore = False


# The on step part
def onStep(app):
    
    # This counter is only for showing the timer in the challenge gameplay page
    if app.challenge_gamePlayPage == True:
        checkChallenge(app)

    if app.challenge_gamePlayPage == True:
        app.counter += 1
        if app.challengeMode == 'Easy':
            if app.counter % 50 == 0:
                app.time -= 1
                if app.time <= 0:
                    app.challengeFail = True

        elif app.challengeMode == 'Hard':
            if app.counter % 25 == 0:
                app.time -= 1
                if app.time <= 0:
                    app.challengeFail = True

    if app.challenge_gamePlayPage == True:
        checkPocket_Challenge(app)
    elif app.multi_gamePlayPage == True:
        checkPocket(app)

    if app.multi_gamePlayPage == True:
        checkWinners_1(app)
        checkWinners_2(app)

    if app.Stick.isHitting == True:
        if app.Stick.pullingDistance < 100: # This will make sure it only reach 100
            app.Stick.pullingDistance += 1
            app.Power.updatePower(app.Stick.pullingDistance)

    if app.multi_gamePlayPage == True:
        for ball in app.allBalls:
            ball.updateBallPosition()
    elif app.challenge_gamePlayPage == True:
        for ball in app.easyChallenge:
            ball.updateBallPosition()

    if app.multi_gamePlayPage == True:
        checkCollisonAll(app)

    if app.challenge_gamePlayPage == True:
        checkCollisonChallenge(app)

    if app.multi_gamePlayPage == True:
        if (abs(app.whiteBall.X_velocity) > 0.1 and abs(app.whiteBall.Y_velocity) > 0.1):
            whiteBallCollison(app)


    app.Stick.StickRotate(app.whiteBall.positionX, app.whiteBall.positionY, app.mouseX, app.mouseY)

    if app.multi_gamePlayPage == True:
        if app.needTurnCheck:
            if checkStop(app) == True and app.hitTimes > 0:
                checkForGoalsAndFouls(app)
                app.needTurnCheck = False


# This function is for checking the winner condition (a easy way to check)
def cheatSolid(app):
    # This part is for checking if the ball can be gone and show on the side 
    # (if you want to check this uncomment it and commenet the last line)
    # for ball in app.allSolid:
    #     ball.isPocket = True
    # app.blackBall.isPocket = True

    # quick way to go to the winner page
    app.playerOneIsWinner = True


def cheatStrip(app):
    # This part is for checking if the ball can be gone and show on the side 
    # (if you want to check this uncomment it and commenet the last line)
    # for ball in app.allStrip:
    #     ball.isPocket = True

    # quick way to go to the winner page
    app.playerTwoIsWinner = True

# check the foul
def checkForGoalsAndFouls(app):
    # isScored = checkIfScored()  
    # isFouled = checkIfFouled() 
    isScored = app.isScore
    isFouled = checkIfFouled(app)

    if isFouled or (isScored == False and isFouled == False):
        # switchTurn(app)
        # return True
        if app.currentPlayer == app.PlayerOne:
            app.currentPlayer = app.PlayerTwo
        elif app.currentPlayer == app.PlayerTwo:
            app.currentPlayer = app.PlayerOne

# To check what balls player hit into the hole
def checkGoal(app):
    if app.currentPlayer == app.PlayerOne:
        for ball in app.allPocket:
            if ball.color == 'red' or ball.color == 'white':
                app.allPocket = []
                return True
        return False
            
    elif app.currentPlayer == app.PlayerTwo:
        for ball in app.allPocket:
            if ball.color == 'yellow' or ball.color == 'white':
                app.allPocket = []
                return True
        return False

# Player One should hit the yellow / Player Two should hit the red
def checkIfFouled(app):
    if app.currentPlayer == app.PlayerOne and app.hitTimes > 1:

        # if (checkGoal(app)) or (app.firstCollisionBall == 'black') or (app.firstCollisionBall == 'red') or (app.firstCollisionBall == None):
        #     print('foul this one')
        #     app.whiteBall.isPocket = True
        #     return True

        if app.firstCollisionBall == None:
            app.whiteBall.isPocket = True
            # print('player one foul / because white ball did not hit')
            return True
        elif app.firstCollisionBall == 'red' or app.firstCollisionBall == 'black':
            app.whiteBall.isPocket = True
            # print('player one foul / because hit the red or black first')
            return True
        elif checkGoal(app):
            app.whiteBall.isPocket = True
            # print('player one foul / beacause score the wrong color of ball')
            return True
        else:
            return False

        
    elif app.currentPlayer == app.PlayerTwo and app.hitTimes > 1:

        # if (checkGoal(app)) or (app.firstCollisionBall == 'black') or (app.firstCollisionBall == 'yellow') or (app.firstCollisionBall == None):
        #     print('foul')
        #     app.whiteBall.isPocket = True
        #     return True

        if app.firstCollisionBall == None:
            app.whiteBall.isPocket = True
            # print('player two foul / because white ball did not hit')
            return True
        elif app.firstCollisionBall == 'yellow' or app.firstCollisionBall == 'black':
            app.whiteBall.isPocket = True
            # print('player two foul / because hit the yellow or black first')
            return True
        elif checkGoal(app):
            app.whiteBall.isPocket = True
            # print('player two foul / beacause score the wrong color of ball')
            return True
        else:
            return False
  

def main():
    runApp()

main()
