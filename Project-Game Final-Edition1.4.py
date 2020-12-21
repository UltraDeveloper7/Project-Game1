import turtle
import random
import time
import winsound


wn = turtle.Screen()
wn.bgcolor("black")
def ask_name():
    global Pilot
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
ask_name()
score_count = 0

####################################Classes###################################

class Create_Objects(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.penup()


class Message(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("white")
        self.speed(0)
        self.penup()
        self.hideturtle()



#Set up the player
player = Create_Objects()
turtle.register_shape("player.gif")
player.speed(0)                                    # animation speed of the turtle module
player.shape("player.gif")
player.shapesize(stretch_wid=2, stretch_len=2)
player.goto(0, -280)
playerspeed = 25


#Set up the Player-Laser
Laser = Create_Objects()
turtle.register_shape("Laser.gif")
Laser.shape("Laser.gif")
Laser.speed(0)
Laser.setheading(90)
Laser.shapesize(0.5,0.5)
Laser.goto(0, -400)
Laser.hideturtle()
Laserspeed = 7


#Set up the enemy
enemy = Create_Objects()
turtle.register_shape("Enemy.gif")
enemy.speed(0)
enemy.shape("Enemy.gif")
enemy.setpos(0, 280)
player.shapesize(stretch_wid=4, stretch_len=4)
enemyspeed = 18


#Set up the Enemy-Laser
enemylaser = Create_Objects()
turtle.register_shape("Enemy-Laser.gif")
enemylaser.shape("Enemy-Laser.gif")
enemylaser.speed(0)
enemylaser.setheading(90)
enemylaser.shapesize(0.5, 0.5)
enemylaser.setpos(0, 400)
enemylaser.hideturtle()
enemylaserspeed = 10


#Set up the comets.
#Put any number in the fellow list!
number_of_comets = 5
comets = []
turtle.register_shape("comet.gif")

for _i  in range(number_of_comets):
    comets.append(turtle.Turtle())

for comet in comets:
    comet.shape("comet.gif")
    comet.penup()
    comet.shapesize(stretch_wid=2,stretch_len=2)
    comet.speed(0)
    comet.right(90)
    comet.direction = "down"
    x = random.randint(-400, 400)
    y = random.randint(220, 260)
    comet.setposition(x, y)
cometspeed = 1.5



##################################Functions########################################

#Function for Game Screen
def Start_Game():
    global Game_State
    global Initial_Message
    global instruction_message
    Game_State = "Game"
    wn.bgpic("SpaceBackground.gif")
    player.showturtle()
    enemy.showturtle()
    for c in comets:
        c.showturtle()
    Life_board.write("Lifes: {}".format(lifes), font=("Courier", 24, "normal"))
    if lifes == 1 :
        Life_board.clear()
        Life_board.color("red")
        Life_board.write("Life: {}".format(lifes), font=("Courier", 24, "normal"))
    comet_pen.write(cometstring, False, align = "Left", font = ("Courier", 24, "normal"))



#Function for Instruction Screen
def Instructions():
    global Game_State
    global Initial_Message
    global instruction_message
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
    instruction_message.hideturtle()
    instruction_message.clear()



#Function for Game-Description
def Instructions2():
    global Game_State
    global Initial_Message
    global instruction_message
    Game_State = "Instructions2"
    wn.bgpic("Instructions2.png")
    instruction_message.write(" {},". format(str(Pilot)), font = ("Microsoft 35"))



#Function for Main-Screen
def Main_Screen():
    global Game_State
    global Initial_Message
    Game_State = "Main-Screen"
    wn.bgpic("MainScreen.gif")
    player.hideturtle()
    enemy.hideturtle()
    for c in comets:
        c.hideturtle()
    comet_pen.clear()
    comet_pen.hideturtle()
    Life_board.hideturtle()
    Life_board.clear()
    Initial_Message.write("Welcome {}!!". format(str(Pilot)), align = "center", font = ("Courier", 40, "normal"))
    instruction_message.hideturtle()
    instruction_message.clear()



#Function for End Screen
def End_Game():
    global Game_State
    Game_State = "Game - Over"
    wn.bgpic("Game_Over.gif")
    winsound.PlaySound("Game-Over.wav", winsound.SND_ASYNC)
    player.hideturtle()
    enemy.hideturtle()
    Laser.hideturtle()
    enemylaser.hideturtle()
    for c in comets:
        c.hideturtle()



#Function for Paused Screen
is_paused = False
def toggle_pause():
    global is_paused
    global Game_State
    if is_paused == True:
        is_paused = False
    else:
        is_paused = True
    Game_State = "Paused"



#Function for Quit Screen
def Quit():
    global running
    running = False


#Make the player move
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 370:
        x = 370
    player.setx(x)

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
        enemyspeed *= - 1
    if x < -370:
        enemyspeed *= -1


#Make comets move
def move_comet():
    global score_count
    for comet in comets:
        if comet.direction =="down":
            y = comet.ycor()
            y -= cometspeed
            comet.sety(y)
            if comet.ycor() <= -270:
                y = comet.ycor()
                y -= 2
                comet.sety(y)
                if comet.ycor() <= -275 and Game_Over == False and Victory == False:
                    comet.hideturtle()
                    x = random.randint(-400, 400)
                    y = random.randint(100, 250)
                    comet.setposition(x, y)
                    comet.showturtle()
                    score_count += 0.5



#Make Laser Move
def move_Laser():
    global Laserstate
    #Move Laser
    if Laserstate == "fire":
        y = Laser.ycor()
        y += Laserspeed
        Laser.sety(y)
    #Check Laser΄s position
    if Laser.ycor() >= 260:
        Laser.hideturtle()
        Laser.goto(0, -400)
        Laserstate = "ready"


#Make Enemy-Laser Move
def move_enemylaser():
    global Lasersituation
    #Move Laser
    if Lasersituation == "fire":
        y = enemylaser.ycor()
        y -= enemylaserspeed
        enemylaser.sety(y)
    #Check enemy's Laser position
    if enemylaser.ycor() < - 290:
        enemylaser.hideturtle()
        enemylaser.goto(0, 400)
        Lasersituation = "ready"


#Check for collision(comet,laser)
def collide(comet, laser):
    distance = comet.distance(laser)
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


#Make Laser able to fire
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




###############################Screen update############################
def Screen():
    #Set up the screen
    Screen_Width = 1000
    Screen_Height = 800
    wn.title("Comet crasher")
    wn.bgcolor("black")
    wn.setup(Screen_Width + 40, Screen_Height + 40)
    wn.cv._rootwindow.resizable(False, False)
    wn.tracer(0)             # turns off screen updates and makes the turtle go as fast as possible
    BorderPen = Message()
    BorderPen.setposition(-500,400)
    BorderPen.pendown()
    BorderPen.pensize(3)
    BorderPen.fd(1000)
    BorderPen.rt(90)
    BorderPen.fd(800)
    BorderPen.rt(90)
    BorderPen.fd(1000)
    BorderPen.rt(90)
    BorderPen.fd(800)
    BorderPen.hideturtle()
    BorderPen.penup()

Screen()

def init_message():
    global Initial_Message
    #Welcome Message
    Initial_Message = Message()
    Initial_Message.setpos(5,180)
    Initial_Message.write("Welcome {}!!". format(str(Pilot)), align = "center", font = ("Courier", 40, "normal"))

init_message()

def sec_message():
    global instruction_message
    #Instruction Message
    instruction_message = Message()
    instruction_message.setpos(-320, 195)
    instruction_message.write(" {},". format(str(Pilot)), font = ("Microsoft 35"))

sec_message()

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


#Keyboard bindings
wn.listen()
wn.onkeypress(move_right,"Right")
wn.onkeypress(move_left,"Left")
wn.onkeypress(fire_Laser, "space")
wn.onkeypress(Start_Game, "S")
wn.onkeypress(Start_Game, "s")
wn.onkeypress(toggle_pause, "p")
wn.onkeypress(toggle_pause, "P")
wn.onkeypress(toggle_pause, "c")
wn.onkeypress(toggle_pause, "C")
wn.onkeypress(Instructions, "F")
wn.onkeypress(Instructions, "f")
wn.onkeypress(Instructions, "Up")
wn.onkeypress(Instructions2, "Down")
wn.onkeypress(Quit, "Q")
wn.onkeypress(Quit, "q")


##############################Main game loop#########################

#Indication that the Laser is ready to fire
Laserstate= "ready"
Lasersituation="ready"
Game_Over = False
Victory = False
Game_State = "Main-Screen"
running = True
while running :

    wn.update()      #everytime it goes into the loop it updates the screen

    if Comet != 100 :

            if lifes > 0:

                if not is_paused:
                    #First Screen
                    if Game_State == "Main-Screen":
                        Main_Screen()



                    #Instructions Screen
                    if Game_State == "Instructions":
                        Initial_Message.hideturtle()
                        Initial_Message.clear()
                        Instructions()
                        if Game_State == "Instructions2":
                            Initial_Message.hideturtle()
                            Initial_Message.clear()
                            Instructions2()



                    #Main Screen
                    if Game_State == "Game":
                        is_paused = False
                        Initial_Message.hideturtle()
                        Initial_Message.clear()
                        instruction_message.hideturtle()
                        instruction_message.clear()
                        Start_Game()



                        move_enemy()
                        move_enemylaser()
                        fire_enemylaser()



                        #Check collision between Enemy-Laser and player
                        if crash(player, enemylaser):
                            winsound.PlaySound("Enemy-Crash.wav", winsound.SND_ASYNC)
                            lifes -= 1
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
                            #Update Lifes
                            if lifes > 1:
                                Life_board.clear()
                                Life_board.color("white")
                                Life_board.write("Lifes: {}".format(lifes), font=("Courier", 24, "normal"))
                            if lifes == 1:
                                Life_board.clear()
                                Life_board.color("red")
                                Life_board.write("Life: {}".format(lifes), font=("Courier", 24, "normal"))
                            comet_pen.write(cometstring, False, align = "Left", font = ("Courier", 24, "normal"))



                        for comet in comets:
                            move_comet()



                            #Check collision between Laser and comet
                            if  collide(Laser , comet):
                                winsound.PlaySound("Collision 2.wav", winsound.SND_ASYNC)
                                cometspeed += 0.005
                                #Reset Laser
                                Laser.hideturtle()
                                Laser.goto(0, -400)
                                Laserstate="ready"
                                #Reset comet
                                x = random.randint(-280, 280)
                                y = random.randint(100, 250)
                                comet.setposition(x, y)
                                #Update score
                                Comet += 1
                                if Comet == 0 or Comet == 1:
                                    comet_pen.color("lightblue")
                                    cometstring = "Comet: {}".format(Comet)
                                    comet_pen.clear()
                                    comet_pen.write(cometstring, False, align = "Left", font = ("Courier", 24, "normal"))
                                else:
                                    comet_pen.color("lightblue")
                                    cometstring = "Comets: {}".format(Comet)
                                    comet_pen.clear()
                                    comet_pen.write(cometstring, False, align = "Left", font = ("Courier", 24, "normal"))



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
                            Life_board.write("Lifes: {}".format(lifes), font=("Courier", 24, "normal"))
                            if lifes == 1 or lifes == 0:
                                Life_board.clear()
                                Life_board.color("red")
                                Life_board.write("Life: {}".format(lifes), font=("Courier", 24, "normal"))
                            comet_pen.write(cometstring, False, align = "Left", font = ("Courier", 24, "normal"))



            else:
                lifes == 0
                Game_Over = True
                restart_game = True
                if Game_Over == True and running == True  :
                    End_Game()
                    comet_pen.clear()
                    comet_pen.hideturtle()
                    Life_board.hideturtle()
                    Life_board.clear()
                    wn.update()
                    message = Message()
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

                    wn.exitonclick()




    else:
        #Put comet == 10 for test and only!
        Comet == 100
        Victory = True
        if Victory == True and running == True :
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
            comet_pen.hideturtle()
            Life_board.hideturtle()
            Life_board.clear()
            wn.update()
            message.write(" {} you are the winner!!".format(str(Pilot)), \
                          align = "center", font = ("Courier", 40, "normal"))
            message2.write("Click anywhere to exit!", align = "center", font = ("Courier" ,30, "normal"))

            wn.exitonclick()



#synchronized  with Quit Button
wn.bye()

