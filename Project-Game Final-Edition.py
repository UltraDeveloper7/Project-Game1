import turtle
import random
import time
import winsound


wn = turtle.Screen()    # Main window where the game is evolved
wn.bgcolor("black")
Pilot = wn.textinput("Welcome Player!!", "Please write your name in the space below:").capitalize()
if Pilot == '':
    Pilot = 'Pilot'
if "ς"  in Pilot and   Pilot[-2] == "ο" and len(Pilot) == 6 or len(Pilot) == 5 or len(Pilot) == 7:
    Pilot = Pilot.rstrip("ς")
if  "ς"  in Pilot and Pilot[-2] =="η" or Pilot[-2] == "ή":
    Pilot = Pilot.rstrip("ς")
if  "ς"  in Pilot and Pilot[-2] =="α":
    Pilot = Pilot.rstrip("ς")
if "ς"  in Pilot and   Pilot[-2] == "ο" and len(Pilot) > 6:
    Pilot = Pilot.rstrip("ς").replace(Pilot[-2], "ε")
else:
    Pilot

score_count = 0

####################################Classes###################################

class Create_Objects(turtle.Turtle):   # Creates the objects: player, Player-Laser, enemy, Enemy-Laser
    def __init__(self):
        turtle.Turtle.__init__(self)  # We use an object of the class, the turtle.Turtle as a method
        self.speed("fastest")      # Makes the turtle go as fast as possible
        self.penup()        # It prompts the turtle not to leave marks


class Message(turtle.Turtle):    # Creates the objects: Border for the screen, Welcome Message, Instruction Message, Comet, Lifes
    def __init__(self):
        turtle.Turtle.__init__(self) 
        self.color("white")   # we give to the turtle an initial white color
        self.speed("fastest") 
        self.penup()
        self.hideturtle()  # we do not want to see the turtle as is but the messages that it creates


###########################Create some objects from the classes above########################

#Set up the player
player = Create_Objects()
turtle.register_shape("player.gif")        # We register a shape for the turtle
player.speed(0)                                    # animation speed of the turtle module
player.shape("player.gif")                    # We define finally the shape of the turtle
player.shapesize(stretch_wid=2, stretch_len=2)  # we stretch the turtle in the x,y dimension
player.goto(0, -280)   # We set the player turtle to the possition (0,-280)
playerspeed = 25  # We  set the speed of the player turtle


#Set up the Player-Laser
Laser = Create_Objects()
turtle.register_shape("Laser.gif")
Laser.shape("Laser.gif")
Laser.speed(0)
Laser.setheading(90)   # We set the turtle vertically to the x axis
Laser.shapesize(0.5,0.5)
Laser.goto(0, -400)   # We want the footprint of the turtle to begin from the position (0, -400)
Laser.hideturtle()
Laserspeed = 3


#Set up the enemy
enemy = Create_Objects()
turtle.register_shape("Enemy.gif")
enemy.speed(0)
enemy.shape("Enemy.gif")
enemy.setpos(0, 280)
player.shapesize(stretch_wid=4, stretch_len=4)
enemyspeed = 7


#Set up the Enemy-Laser
enemylaser = Create_Objects()
turtle.register_shape("Enemy-Laser.gif")
enemylaser.shape("Enemy-Laser.gif")
enemylaser.speed(0)
enemylaser.setheading(90)
enemylaser.shapesize(0.5, 0.5)
enemylaser.setpos(0, 400)
enemylaser.hideturtle()
enemylaserspeed = 5



#Set up the screen
Screen_Width = 1000
Screen_Height = 800
wn.title("Comet crasher")
wn.bgcolor("black")
wn.setup(Screen_Width + 40, Screen_Height + 40)
wn.cv._rootwindow.resizable(False, False)   # It makes the window non resizable
wn.tracer(0)             # turns off screen updates and makes the turtle go as fast as possible
BorderPen = Message()
BorderPen.setposition(-500,400)
BorderPen.pendown()  # it puts the pen-turtle down to the canvas and prepares it to draw
BorderPen.pensize(3)  # it determines the pen width
BorderPen.fd(1000)  
BorderPen.rt(90)
BorderPen.fd(800)
BorderPen.rt(90)
BorderPen.fd(1000)
BorderPen.rt(90)
BorderPen.fd(800)
BorderPen.hideturtle()
BorderPen.penup()




#Welcome Message
Welcome_Message = Message()
Welcome_Message.setpos(5,180)
Welcome_Message.write("Welcome {}!!". format(str(Pilot)), align = "center", font = ("Courier", 40, "normal"))




#Instruction Message 
Instruction_Message = Message()
Instruction_Message.setpos(-320, 195)
Instruction_Message.write(" {},". format(str(Pilot)), font = ("Microsoft 35"))



#Comet crash
Comet=0
comet_pen = Message()
comet_pen.color("lightblue")
comet_pen.setposition(-470,360)
cometstring = "Comet: {}". format(Comet)
comet_pen.write(cometstring, False, align = "Left", font = ("Courier", 24, "normal"))


#Lifes
lifes = 3
Life_board = Message()
Life_board.goto(320,360)
Life_board.write("Lifes: {}".format(lifes), font=("Courier", 24, "normal"))





#Set up the comets.
number_of_comets = 5
comets = []  # We create an empty list which throughout the process will be filled with turtles
turtle.register_shape("comet.gif")

for _i  in range(number_of_comets): # We append finally the turtles to the list
    comets.append(turtle.Turtle())

for comet in comets:  # For every turtle in the list we attribute some features
    comet.shape("comet.gif")
    comet.penup()
    comet.shapesize(stretch_wid=2,stretch_len=2)
    comet.speed(0)
    comet.direction = "down"
    x = random.randint(-400, 400)
    y = random.randint(220, 260)
    comet.setposition(x, y)
cometspeed = 0.7



##################################Functions########################################

#Function for Main-Screen
def Main_Screen():   # when the Main_Screen() is being called, an initial splash screen is being shown
    global Game_State 
    global Welcome_Message
    Game_State = "Main-Screen" # in the main game loop that particular instruction constitute a former check so as for the turtle module to understand where to draw
    wn.bgpic("MainScreen.gif")  # it uploads the certain background pic
    player.hideturtle()   # since turtle module  is a drawing graphical environment it can not be used to draw seperate screens for a game but it can be used for overlapping the main window with others
    enemy.hideturtle()            ### with the following instructions we create an illusion be hiding all the comets ,players or enemies from the Main-Screen
    for c in comets:                
        c.hideturtle()
    comet_pen.clear()
    comet_pen.hideturtle()             
    Life_board.hideturtle()
    Life_board.clear()
    Welcome_Message.write("Welcome {}!!". format(str(Pilot)), align = "center", font = ("Courier", 40, "normal"))
    Instruction_Message.hideturtle()
    Instruction_Message.clear() 



#Function for Instruction Screen
def Instructions():
    global Game_State
    global Welcome_Message
    global Instruction_Message
    Game_State = "Instructions" 
    wn.bgpic("Instructions.png")
    player.hideturtle()
    enemy.hideturtle()
    for c in comets:
        c.hideturtle()
    comet_pen.clear()
    comet_pen.hideturtle()
    Life_board.hideturtle()
    Life_board.clear()
    Instruction_Message.hideturtle()
    Instruction_Message.clear()




#Function for Game-Description
def Instructions2():
    global Game_State
    global Welcome_Message
    global Instruction_Message
    Game_State = "Instructions2"
    wn.bgpic("Instructions2.png")
    Instruction_Message.write(" {},". format(str(Pilot)), font = ("Microsoft 35"))




#Function for Game Screen
def Start_Game():
    global Game_State
    global Welcome_Message
    global Instruction_Message
    Game_State = "Game"
    wn.bgpic("SpaceBackground.gif") 
    player.showturtle()     # finally when the player starts the game we appear all the comets the player and the enemy again to the main window screen 
    enemy.showturtle()
    for c in comets:
        c.showturtle()
    Life_board.write("Lifes: {}".format(lifes), font=("Courier", 24, "normal"))
    if lifes == 1 :
        Life_board.clear()
        Life_board.color("red")
        Life_board.write("Life: {}".format(lifes), font=("Courier", 24, "normal"))
    comet_pen.write(cometstring, False, align = "Left", font = ("Courier", 24, "normal"))




#Function for Paused Screen
is_paused = False   # initially the global variable is_paused is False which means that the game is not paused
def toggle_pause():  
    global is_paused
    global Game_State 
    if is_paused == True:   # every time the is_paused is True we change it rapidly to False
        is_paused = False
    else:
        is_paused = True
    Game_State = "Paused"



#Function for End Screen
def End_Game():
    global Game_State
    Game_State = "Game - Over"
    wn.bgpic("Game_Over.gif")
    winsound.PlaySound("Game-Over.wav", winsound.SND_ASYNC)   #through the winsound module and the variable PlaySound we play asychronous a particular sound 
    player.hideturtle()
    enemy.hideturtle()
    Laser.hideturtle()
    enemylaser.hideturtle()
    for c in comets:
        c.hideturtle()



#Function for Quit Screen
def Quit():
    global running 
    running = False  #in the Quit function running is False which means that by the time which the Quit function is being called the game stops running and we can exit the game




#Make the player move
def move_right():
    x = player.xcor()  # the coordination of the player in the x axis 
    x += playerspeed #move the player 25 pixels from the x.coordinate which he is 
    if x > 370:  # a simple check for the borders of the game
        x = 370
    player.setx(x) # sets the player-turtle every time in the x coordinate which has been determined earlier

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -370:
        x = -370
    player.setx(x)



#Make the Enemy move right and left
def move_enemy():
    global enemyspeed
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)
    if x > 370:
        enemyspeed *= - 1  # it moves the enemy-turtle to the opposite direction
    if x < -370:
        enemyspeed *= -1 # the same with the above instruction



#Make comets move
def move_comet():
    global score_count
    for comet in comets:  
        if comet.direction =="down":  # variable for the direction of the comets
            y = comet.ycor()
            y -= cometspeed  
            comet.sety(y)
            if comet.ycor() <= -270:  
                y = comet.ycor()
                y -= 2
                comet.sety(y)
                if comet.ycor() <= -275 and Game_Over == False and Victory == False:  # some early checks for the game condition 
                    comet.hideturtle() # if the above sentence is True then hide the turtle-comet 
                    x = random.randint(-400, 400)   # the range of the x axis where the turtle can be reset 
                    y = random.randint(100, 250)    # the range of y axis where the turtle can be reset
                    comet.setposition(x, y)    # the  precise position  which will be placed
                    comet.showturtle()  # show the turtle_comet again
                    score_count += 0.1



#Make Player - Laser Move
def move_Laser():
    global Laserstate
    #Move Laser
    if Laserstate == "fire":  # the condition of the laser when you are allowed to shoot
        y = Laser.ycor()
        y += Laserspeed
        Laser.sety(y)
    #Check Laser΄s position
    if Laser.ycor() >= 280: 
        Laser.hideturtle()
        Laser.goto(0, -400)
        Laserstate = "ready"  # the condition of the laser when it has been prepared and it is ready to fire



#Make Enemy-Laser Move
def move_enemylaser():
    global Lasersituation
    #Move Laser
    if Lasersituation == "fire":
        y = enemylaser.ycor()
        y -= enemylaserspeed
        enemylaser.sety(y)
    #Check enemy's Laser position
    if enemylaser.ycor() < - 350:
        enemylaser.hideturtle()
        enemylaser.goto(0, 400)
        Lasersituation = "ready"



#Check for collision(comet,laser)
def collide(comet, laser):
    distance = comet.distance(laser)  # the distance between comet-laser which is a boolean variable
    if distance <= 30:  
        return True
    else:
        return False



#Check for collision(comet,player)
def crash(comet, player):
    distance = comet.distance(player)
    if distance <= 25:
        return True
    else:
        return False



#Make Player-Laser able to fire
def fire_Laser():
    global Laserstate
    if Laserstate=="ready":
        Laserstate = "fire"
        winsound.PlaySound("Laser.wav", winsound.SND_ASYNC)
        # Move Laser right above player
        x = player.xcor()
        y = player.ycor() + 10
        Laser.setposition(x, y)
        Laser.showturtle()



#Make the Enemy-Laser able to fire
def fire_enemylaser():
    global Lasersituation
    if Lasersituation=="ready":
        Lasersituation = "fire"
        winsound.PlaySound("Enemy-Laser.wav", winsound.SND_ASYNC)
        # Move Laser right above player
        x = enemy.xcor()
        y = enemy.ycor() - 10
        enemylaser.setposition(x, y)
        enemylaser.showturtle()




#Keyboard bindings from which you can control the whole game panels and the game generally
wn.listen()
wn.onkeypress(Start_Game, "S")
wn.onkeypress(Start_Game, "s")
wn.onkeypress(Instructions, "F")
wn.onkeypress(Instructions, "f")
wn.onkeypress(Instructions, "8")
wn.onkeypress(Instructions2, "2")
wn.onkeypress(move_right,"Right")
wn.onkeypress(move_left,"Left")
wn.onkeypress(fire_Laser, "space")
wn.onkeypress(toggle_pause, "p")
wn.onkeypress(toggle_pause, "P")
wn.onkeypress(toggle_pause, "c")
wn.onkeypress(toggle_pause, "C")
wn.onkeypress(Quit, "Q")
wn.onkeypress(Quit, "q")


##############################Main game loop#########################

# Indication that the Laser is ready to fire
Laserstate= "ready"
Lasersituation="ready"
# Indication that the Game has come to it's End
Game_Over = False
Victory = False
#Initially the Game_State and therefore what the player can actually see is the first-splash-main screen
Game_State = "Main-Screen"
# Indication that Game still running
running = True
while running :

    wn.update()  # refreshes the game window and adds any new update to the screen

    if Comet != 100 :  
        

        if lifes > 0:

            if  not is_paused :
                #First Screen
                if Game_State == "Main-Screen":
                    Main_Screen()



                #Instructions Screen
                if Game_State == "Instructions":
                    Welcome_Message.clear()  # Erase the Welcome_Message and simultaneously hide the turtle which has drawn it
                    if Game_State == "Instructions2":
                        Welcome_Message.clear()




                #Main Screen
                if Game_State == "Game":
                    is_paused = False
                    Welcome_Message.clear()
                    Instruction_Message.clear()


                    wn.update()
                    
                


                    move_enemy()  # call the function move_enemy()
                    move_enemylaser() # call the function move_enemylaser()
                    fire_enemylaser()  # call the function fire_enemylaser()



                    #Check collision between Enemy-Laser and player
                    if crash(player, enemylaser): # check what the boolean variable returns
                        winsound.PlaySound("Enemy-Crash.wav", winsound.SND_ASYNC)
                        lifes -= 1 # subtract  one life from the current amount
                        #Reset Laser
                        enemylaser.hideturtle()
                        enemylaser.setpos(0, 400)
                        Lasersituation="ready"
                        #Update Lifes
                        Life_board.clear()
                        Life_board.write("Lifes: {}".format(lifes), font=("Courier", 24, "normal"))



                    #Check collision between Laser and enemy
                    if collide(Laser, enemy):
                        winsound.PlaySound("Crash.wav", winsound.SND_ASYNC)
                        lifes += 1
                        #Reset Laser
                        Laser.hideturtle()
                        Laser.goto(0, -400)
                        Laserstate="ready"
                       


                    for comet in comets:
                        move_comet()  # for every comet in the comets list call the move_comet() function





                        #Check collision between Laser and comet
                        if  collide(Laser , comet):
                            Comet += 1 # icrease by one the current amount
                            winsound.PlaySound("Collision 2.wav", winsound.SND_ASYNC)
                            cometspeed += 0.005 # increase the comet speed every time yours spaceship demolishes a comet
                            #Reset Laser
                            Laser.hideturtle()
                            Laser.goto(0, -400)
                            Laserstate="ready"
                            #Reset comet
                            x = random.randint(-280, 280)
                            y = random.randint(100, 250)
                            comet.setposition(x, y)
                            
                           



                        #Check collision between player and comet
                        if crash(player, comet):
                            winsound.PlaySound("Collision.wav", winsound.SND_ASYNC)
                            comet.hideturtle()
                            lifes -= 1
                            #Reset comet
                            x = random.randint(-280, 280)
                            y = random.randint(100, 250)
                            comet.setposition(x, y)
                            #Update Lifes
                            Life_board.clear()
                            Life_board.write("Lifes: {}".format(lifes), font=("Courier", 24, "normal"))


                        move_Laser()


                    #Update Lifes
                    if lifes > 1:
                        Life_board.clear()
                        Life_board.color("white")
                        Life_board.write("Lifes: {}".format(lifes), font=("Courier", 24, "normal"))
                    if lifes == 1:
                        Life_board.clear()
                        Life_board.color("red")
                        Life_board.write("Life: {}".format(lifes), font=("Courier", 24, "normal"))


                    #Update score
                    if Comet == 0 or Comet == 1:
                        comet_pen.color("lightblue")
                        cometstring = "Comet: {}".format(Comet)
                        comet_pen.clear()
                        comet_pen.write(cometstring, False, align = "Left", font = ("Courier", 24, "normal")) # -----.write(argument, move = True/False, align = -----, font = -----)
                    else:
                        comet_pen.color("lightblue")
                        cometstring = "Comets: {}".format(Comet)
                        comet_pen.clear()
                        comet_pen.write(cometstring, False, align = "Left", font = ("Courier", 24, "normal"))

                       


                if Game_State == "Game - Over":
                    End_Game()
                    


            else:
                #Pause Screen
                if Game_State == "Paused":      ## call the is_paused function and pop up a paused screen window!
                    wn.bgpic("Pause.gif")
                    player.hideturtle()
                    enemy.hideturtle()
                    Laser.hideturtle()
                    enemylaser.hideturtle()
                    for c in comets:
                        c.hideturtle()
                    comet_pen.clear()
                    comet_pen.hideturtle()
                    Life_board.hideturtle()
                    Life_board.clear()
                    wn.update()
                    if not is_paused:          ## on key bind "c" call the Start_Game func to return to gameplay screen!
                        Game_State = "Game"
                        wn.bgpic("SpaceBackground.gif")
                        player.showturtle()
                        enemy.showturtle()
                        Laser.showturtle()
                        enemylaser.showturtle()
                        for c in comets:
                            c.showturtle()




        else:
            lifes == 0
            Game_Over = True
            if Game_Over == True and running == True  : # if these two boolean variables return True, then do the below actions:
                End_Game()
                comet_pen.clear()
                Life_board.clear()
                wn.update()
                message = Message()  # all the messages are subjects of the class Message()
                message1 = Message()
                message2 = Message()
                message.goto(0,-40)
                message1.goto(0, -100)
                message2.goto(0, - 140)
                message4 = Message()
                message4.goto(0, -330)
                message4.write("Click anywhere to exit!", align = "center", font = ("Courier" ,30, "normal"))


                if str(int(score_count)) == '1' or Comet == 1 :
                    message.write('Your Score is: {}'.format(str(int(score_count))), \
                                    align = "center", font = ("Courier", 45, "normal"))
                    message1.write("You΄ve crashed {} comet.". format(Comet), \
                                    align = "center", font = ("Courier", 45, "normal"))
                    message2.write("You could be much better next time {}".format(str(Pilot)), \
                                    align = "center", font = ("Courier", 25, "normal"))

                elif  20 == Comet < 100:
                    message.write("Great job {}!!". format(str(Pilot)), \
                                    align = "center", font = ("Courier", 45, "normal"))
                    message1.write('Your Score is: {} '.format(str(int(score_count))), \
                                    align = "center", font = ("Courier", 45, "normal"))
                    message2.write( "You΄ve crashed {} comets.". format(Comet), \
                                    align = "center", font = ("Courier", 25, "normal"))

                elif Comet == 0:
                    message.write('Your  Score is: {}'.format(str(int(score_count))), \
                                    align = "center", font = ("Courier", 45, "normal"))
                    message1.write("You didn΄t crash any comet!", \
                                    align = "center", font = ("Courier", 45, "normal"))
                    message2.write("You could be much better next time {}!". format(str(Pilot)), \
                                    align = "center", font = ("Courier", 25, "normal"))

                else:
                    message.write('Your Score is: {}'.format(str(int(score_count))),  \
                                    align = "center", font = ("Courier", 45, "normal"))
                    message1.write("You΄ve crashed {} comets.". format(Comet), \
                                    align = "center", font = ("Courier", 45, "normal"))
                    message2.write("Anyone can be overcomed,so keep practicing {}!!". format(str(Pilot)), \
                                    align = "center", font = ("Courier", 20, "normal"))

                wn.exitonclick()  # if the player click on the screen the game will automatically close




    else:
        #Put comet == 10 for test and only!
        Comet == 100
        Victory = True
        if Victory == True and running == True : # if these two boolean variables return True, then do the below actions:
            winsound.PlaySound("Victory.wav", winsound.SND_ASYNC)
            wn.bgpic("End.gif")
            message = Message()
            message2 = Message()
            message2.goto(0, -330)
            player.hideturtle()
            enemy.hideturtle()
            Laser.hideturtle()
            enemylaser.hideturtle()
            for c in comets:
                c.hideturtle()
            comet_pen.clear()
            Life_board.clear()
            wn.update()
            message.write(" {} you are the winner!!".format(str(Pilot)), \
                          align = "center", font = ("Courier", 40, "normal"))
            message2.write("Click anywhere to exit!", align = "center", font = ("Courier" ,30, "normal"))

            wn.exitonclick()



#synchronized  with Quit Button
wn.bye() 
 
