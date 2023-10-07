import turtle

tina = turtle.Turtle()
myscreen = turtle.Screen()
head_finished = False
body_finished = False
beak_finished = False
eye_finished = False
tail_finished = False
lleg_finished = False
rleg_finished = False
background_finished = False

# to do:
# glitch: select one body part, don't fill in color, select another
# will fill in first body part but not second

# credit: printing a paragraph break found at
# https://stackoverflow.com/questions/5982206/how-to-print-a-linebreak-in-a-python-function
# use /n at the end of what you want to print, before the closing quote

# debug program:


def debugclicky(x, y):
    # use this to see where a coordinate is
    tina.penup()
    tina.goto(x, y)
    print(x, y)


def clicky(x, y):
    while True:
        whatcolor = input("What color will you use?\n")
        tina.setheading(0)
        tina.color("black")
        tina.penup()
        tina.goto(x, y)

        # color the beak
        if 130 > x > 93 and 127 > y > 110:
            def colorbeak():
                tina.penup()
                tina.fill(True)
                tina.goto(110, 130)
                tina.setheading(-40)
                tina.forward(30)
                tina.setheading(-180)
                tina.forward(40)
                tina.setheading(50)
                tina.forward(29)
                tina.color(whatcolor)
                tina.pendown()
                tina.fill(False)
                print(
                    "That does it for the beak - but if you haven't colored the head yet, you'll have to recolor this.")
                tina.penup()
            colorbeak()
            beak_finished = True
            break

           # color the eye
        elif 63 > x > 60 and 152 > y > 138:
            def coloreye():
                tina.penup()
                tina.fill(True)
                tina.goto(60, 155)
                tina.setheading(-10)
                tina.forward(5)
                tina.setheading(-90)
                tina.forward(15)
                tina.setheading(-190)
                tina.forward(5)
                tina.setheading(90)
                tina.forward(15)
                tina.color(whatcolor)
                tina.pendown()
                tina.fill(False)
                print(
                    "The eye is finished - but if you haven't colored the head yet, you'll have to recolor this.")
                tina.penup()
            coloreye()
            eye_finished = True
            break

        # color the head
        elif 122 > x > 24 and 190 > y > 95:
            def colorhead():
                tina.penup()
                tina.fill(True)
                tina.goto(75, 95)
                tina.setheading(0)
                tina.circle(50)
                tina.color(whatcolor)
                tina.pendown()
                tina.fill(False)
                tina.penup()

                # recolor the beak
                tina.penup()
                tina.fill(True)
                tina.goto(110, 130)
                tina.setheading(-40)
                tina.forward(30)
                tina.setheading(-180)
                tina.forward(40)
                tina.color("white")
                tina.pendown()
                tina.fill(False)
                tina.penup()
                beak_finished = False

                # recolor in the eye
                tina.penup()
                tina.fill(True)
                tina.goto(60, 155)
                tina.setheading(-10)
                tina.forward(5)
                tina.setheading(-90)
                tina.forward(15)
                tina.setheading(-190)
                tina.forward(5)
                tina.setheading(90)
                tina.forward(15)
                tina.color("white")
                tina.pendown()
                tina.fill(False)
                print("That's the head done.")
                tina.penup()
                eye_finished = False
            colorhead()
            head_finished = True
            break

        # color the body
        elif 88 > x > -120 and 95 > y > -45:
            def colorbody():
                tina.penup()
                print("Just wait a second...")
                tina.fill(True)
                tina.goto(29, 121)
                tina.setheading(-30)
                tina.forward(61)
                tina.setheading(0)
                tina.right(70)
                tina.forward(82)
                for i in range(100):
                    tina.right(1)
                    tina.forward(1)
                tina.setheading(180)
                tina.forward(40)
                tina.right(5)
                tina.forward(5)
                tina.right(20)
                tina.forward(108)
                tina.right(40)
                tina.forward(100)
                tina.setheading(10)
                tina.forward(65)
                tina.forward(65)
                tina.left(40)
                tina.forward(38)
                tina.color(whatcolor)
                tina.pendown()
                tina.fill(False)
                print("The body is colored in.")
                tina.penup()
            colorbody()
            body_finished = True
            break

        # color the left leg
        elif 20 > x > -36 and -46 > y > -127:
            def colorleftleg():
                tina.penup()
                tina.goto(-20, -45)
                tina.fill(True)
                tina.setheading(-90)
                tina.forward(50)
                tina.setheading(170)
                tina.forward(10)
                tina.left(5)
                tina.forward(7)
                tina.left(120)
                tina.forward(10)
                tina.setheading(-10)
                tina.forward(15)
                tina.right(15)
                tina.forward(15)
                tina.right(15)
                tina.forward(20)
                tina.right(5)
                tina.forward(7)
                tina.left(120)
                tina.forward(7)
                tina.left(40)
                tina.forward(15)
                tina.left(40)
                tina.forward(20)
                tina.setheading(5)
                tina.forward(15)
                tina.right(40)
                tina.forward(15)
                tina.right(40)
                tina.forward(20)
                tina.left(160)
                tina.forward(20)
                tina.left(50)
                tina.forward(20)
                tina.left(50)
                tina.forward(25)
                tina.setheading(90)
                tina.forward(48)
                tina.color(whatcolor)
                tina.pendown()
                tina.fill(False)
                print("The left leg is done!")
                tina.penup()
            colorleftleg()
            lleg_finished = True
            break

        # color the right leg
        elif 80 > x > 25 and -65 > y > -119:
            def colorrightleg():
                tina.penup()
                tina.goto(40, -64)
                tina.fill(True)
                tina.setheading(-90)
                tina.forward(20)
                tina.setheading(170)
                tina.forward(10)
                tina.left(5)
                tina.forward(7)
                tina.left(120)
                tina.forward(10)
                tina.setheading(-10)
                tina.forward(15)
                tina.right(15)
                tina.forward(15)
                tina.right(15)
                tina.forward(20)
                tina.right(5)
                tina.forward(7)
                tina.left(120)
                tina.forward(7)
                tina.left(40)
                tina.forward(15)
                tina.left(40)
                tina.forward(20)
                tina.setheading(5)
                tina.forward(15)
                tina.right(40)
                tina.forward(15)
                tina.right(40)
                tina.forward(20)
                tina.left(160)
                tina.forward(20)
                tina.left(50)
                tina.forward(20)
                tina.left(50)
                tina.forward(25)
                tina.setheading(90)
                tina.forward(21)
                tina.color(whatcolor)
                tina.pendown()
                tina.fill(False)
                print("The right leg is done!")
                tina.penup()
            colorrightleg()
            rleg_finished = True
            break

        # color the tail
        elif -60 > x > -145 and 148 > y > 75:
            def colortail():
                tina.penup()
                tina.fill(True)
                tina.goto(-120, 73)
                tina.setheading(130)
                tina.forward(30)
                tina.right(20)
                tina.forward(20)
                tina.right(20)
                tina.forward(20)
                tina.right(120)
                tina.forward(20)
                tina.setheading(0)
                tina.forward(5)
                tina.left(75)
                tina.forward(30)
                tina.right(120)
                tina.forward(35)
                tina.setheading(0)
                tina.forward(5)
                tina.left(80)
                tina.forward(20)
                tina.setheading(-50)
                tina.forward(30)
                tina.right(30)
                tina.forward(40)
                tina.setheading(-170)
                tina.forward(70)
                tina.pendown()
                tina.color(whatcolor)
                tina.fill(False)
                print("The tail's colored in!")
                tina.penup()
            colortail()
            tail_finished = True
            break

        # color the background
        else:
            tina.hideturtle
            myscreen.bgcolor(str(whatcolor))
            print("That's the background done.")
            background_finished = True
            break


def setup():
    # draw head
    tina.speed(0)
    tina.penup()
    tina.goto(75, 95)
    tina.setheading(0)
    tina.pendown()
    tina.circle(50)

    # draw body
    tina.penup()
    tina.goto(80, 97)
    tina.pendown()
    tina.right(70)
    tina.forward(90)
    for i in range(100):
        tina.right(1)
        tina.forward(1)
    tina.setheading(180)
    tina.forward(40)
    tina.right(5)
    tina.forward(5)
    tina.right(20)
    tina.forward(110)
    tina.right(40)
    tina.forward(100)
    tina.setheading(10)
    tina.penup()
    tina.forward(65)
    tina.pendown()
    tina.forward(65)
    tina.left(40)
    tina.forward(36)
    tina.penup()

    # draw beak
    tina.goto(110, 130)
    tina.pendown()
    tina.setheading(-40)
    tina.forward(30)
    tina.setheading(-180)
    tina.forward(40)
    tina.penup()

    # draw tail
    tina.speed(0)
    tina.penup()
    tina.goto(-120, 73)
    tina.pendown()
    tina.setheading(130)
    tina.forward(30)
    tina.right(20)
    tina.forward(20)
    tina.right(20)
    tina.forward(20)
    tina.right(120)
    tina.forward(20)
    tina.setheading(0)
    tina.forward(5)
    tina.left(75)
    tina.forward(30)
    tina.right(120)
    tina.forward(35)
    tina.setheading(0)
    tina.forward(5)
    tina.left(80)
    tina.forward(20)
    tina.setheading(-50)
    tina.forward(30)
    tina.right(30)
    tina.forward(40)
    tina.penup()

    # draw left leg
    tina.goto(-20, -45)
    tina.pendown()
    tina.setheading(-90)
    tina.forward(50)
    tina.setheading(170)
    tina.forward(10)
    tina.left(5)
    tina.forward(7)
    tina.left(120)
    tina.forward(10)
    tina.setheading(-10)
    tina.forward(15)
    tina.right(15)
    tina.forward(15)
    tina.right(15)
    tina.forward(20)
    tina.right(5)
    tina.forward(7)
    tina.left(120)
    tina.forward(7)
    tina.left(40)
    tina.forward(15)
    tina.left(40)
    tina.forward(20)
    tina.setheading(5)
    tina.forward(15)
    tina.right(40)
    tina.forward(15)
    tina.right(40)
    tina.forward(20)
    tina.left(160)
    tina.forward(20)
    tina.left(50)
    tina.forward(20)
    tina.left(50)
    tina.forward(25)
    tina.setheading(90)
    tina.forward(48)
    tina.penup()

    # draw right leg
    tina.goto(40, -64)
    tina.pendown()
    tina.setheading(-90)
    tina.forward(20)
    tina.setheading(170)
    tina.forward(10)
    tina.left(5)
    tina.forward(7)
    tina.left(120)
    tina.forward(10)
    tina.setheading(-10)
    tina.forward(15)
    tina.right(15)
    tina.forward(15)
    tina.right(15)
    tina.forward(20)
    tina.right(5)
    tina.forward(7)
    tina.left(120)
    tina.forward(7)
    tina.left(40)
    tina.forward(15)
    tina.left(40)
    tina.forward(20)
    tina.setheading(5)
    tina.forward(15)
    tina.right(40)
    tina.forward(15)
    tina.right(40)
    tina.forward(20)
    tina.left(160)
    tina.forward(20)
    tina.left(50)
    tina.forward(20)
    tina.left(50)
    tina.forward(25)
    tina.setheading(90)
    tina.forward(21)
    tina.penup()

    # draw eye
    tina.goto(60, 155)
    tina.pendown()
    tina.setheading(-10)
    tina.forward(5)
    tina.setheading(-90)
    tina.forward(15)
    tina.setheading(-190)
    tina.forward(5)
    tina.setheading(90)
    tina.forward(15)
    tina.penup()
    tina.hideturtle


setup()
tina.hideturtle()

print("I just finished drawing this chicken, but I don't know what colors to use. Can you help me?")
print("Just click anywhere on the drawing to start!")

try:
    # I realize you're supposed to do something about global variables
    # or something like that to permanently break the loop but for
    # now I'm just going to call it a day
    finished_coloring = False
    while finished_coloring == False:
        myscreen.onclick(clicky)
        if head_finished and body_finished and background_finished and tail_finished and lleg_finished and rleg_finished and eye_finished and beak_finished == True:
            finished_coloring = True
            print("All done!")
            break

except:
    "Error! Something went wrong."

# debug:
# myscreen.onclick(debugclicky)
