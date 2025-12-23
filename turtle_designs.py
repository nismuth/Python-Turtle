# turtle_designs.py: create a constellation drawing with turtle by using functions, main(), filling, circles, parameters

import turtle
qq = turtle.Turtle()  # Giving the turtle an easy name, so it's not annoying to enter over and over
qq.speed(0)  # Set this to 1 if you want to see it slowly draw


def main():  # By using a def main() we can compile all the code into one area - just remember the main() at the bottom
    orion_stamp(-200, 40, 1)  # This is the normal scale of the stamp
    orion_stamp(50, 40, 0.5)  # This is half or 0.5 of normal size


# It's important to organize into functions to make your life a lot easier - just call it and you're good
def orion_stamp(x, y, scale):  # We use the x, y and scale parameters for position and size
    # Here we're making a stamp with the constellation orion on it, inside its own function
    qq.penup()  # Always a good habit to use this before anything
    qq.goto(x, y)  # Here we use the parameter vars and not set numbers so the design dimensions can be changed in post
    qq.pendown()
    # Move to Gradient 1 --------------
    qq.penup()
    qq.left(90)
    qq.forward(150*scale)  # Here we use scale, so we can work off the parameters given to us by the turtle library
    qq.pendown()
    # Gradient 1 --------------
    qq.pencolor("midnight blue")  # For the top of the image, we need to change color first
    qq.fillcolor("midnight blue")  # We also need to tell the turtle to fill in the shape with this color
    qq.begin_fill()  # This is where we tell the turtle this is the beginning of the shape I want to fill
    qq.right(90)
    qq.forward(150*scale)
    qq.right(90)
    qq.forward(50*scale)
    qq.right(90)
    qq.forward(150*scale)
    qq.right(90)
    qq.forward(50*scale)
    qq.end_fill()
    qq.left(180)
    qq.forward(50*scale)
    # Gradient 2 --------------
    qq.left(90)
    qq.pencolor("dark blue")
    qq.fillcolor("dark blue")
    qq.begin_fill()
    qq.forward(150*scale)
    qq.right(90)
    qq.forward(50*scale)
    qq.right(90)
    qq.forward(150*scale)
    qq.right(90)
    qq.forward(50*scale)
    qq.end_fill()
    qq.left(180)
    qq.forward(50*scale)
    # Gradient 3 --------------
    qq.left(90)
    qq.pencolor("medium blue")
    qq.fillcolor("medium blue")
    qq.begin_fill()
    qq.forward(150*scale)
    qq.right(90)
    qq.forward(50*scale)
    qq.right(90)
    qq.forward(150*scale)
    qq.right(90)
    qq.forward(50*scale)
    qq.end_fill()
    # Here is where the constellation drawing begins...
    # Orion graphic setup --------------
    qq.penup()
    qq.goto(x, y)
    qq.right(1)
    qq.forward(2*scale)
    qq.pendown()
    qq.right(90)
    qq.pencolor("white")
    qq.pencolor("white")
    qq.penup()
    qq.left(90)
    qq.forward(96*scale)
    qq.right(90)
    qq.forward(10*scale)
    qq.right(20)
    qq.forward(32*scale)
    qq.pendown()
    qq.right(60)
    qq.left(90)
    qq.penup()
    qq.left(90)
    qq.forward(38*scale)
    qq.pendown()
    # Raised arm --------------
    qq.begin_fill()  # We want to fill in the circle, not leave it empty, that won't look good
    qq.circle(2)  # This is what we'll use to make the little star dots that make up the constellation
    qq.end_fill()  # End fill
    qq.right(175)
    qq.forward(38*scale)
    qq.left(168)
    qq.forward(42*scale)
    qq.begin_fill()
    qq.circle(2)
    qq.end_fill()
    qq.left(180)
    qq.penup()
    qq.forward(42*scale)
    qq.pendown()
    qq.begin_fill()
    qq.circle(2)
    qq.end_fill()
    # Torso --------------
    qq.left(20)
    qq.forward(43*scale)
    qq.begin_fill()
    qq.circle(2)
    qq.end_fill()
    qq.right(20)
    # Legs --------------
    qq.forward(35.5*scale)
    qq.begin_fill()
    qq.circle(2)
    qq.end_fill()
    qq.left(108)
    qq.forward(42*scale)
    qq.left(96)
    qq.begin_fill()
    qq.circle(2)
    qq.end_fill()
    qq.forward(32*scale)
    qq.begin_fill()
    qq.circle(2)
    qq.end_fill()
    # Belt --------------
    qq.left(36)
    qq.forward(10*scale)
    qq.begin_fill()
    qq.circle(2)
    qq.end_fill()
    qq.left(81)
    qq.forward(8*scale)
    qq.begin_fill()
    qq.circle(2)
    qq.end_fill()
    qq.right(23)
    qq.forward(9*scale)
    # Backtrack --------------
    qq.penup()
    qq.left(180)
    qq.forward(9*scale)
    qq.left(23)
    qq.forward(8*scale)
    qq.pendown()
    # Torso right --------------
    qq.left(42)
    qq.forward(30*scale)
    qq.begin_fill()
    qq.circle(2)
    qq.end_fill()
    # Shoulders/head --------------
    qq.left(60)
    qq.forward(15*scale)
    qq.begin_fill()
    qq.circle(2)
    qq.end_fill()
    qq.left(62)
    qq.forward(19*scale)
    # Backtrack
    qq.penup()
    qq.left(180)
    qq.forward(19*scale)
    qq.right(62)
    qq.forward(15*scale)
    qq.pendown()
    # Arm and bow
    qq.left(40)
    qq.forward(43*scale)
    qq.begin_fill()
    qq.circle(2)
    qq.end_fill()
    qq.left(96)
    qq.forward(8*scale)
    qq.begin_fill()
    qq.circle(2)
    qq.end_fill()
    qq.left(10)
    qq.forward(39*scale)
    qq.begin_fill()
    qq.circle(2)
    qq.end_fill()
    # Backtrack
    qq.left(180)
    qq.forward(39*scale)
    qq.right(10)
    qq.forward(8*scale)
    qq.right(8)
    qq.forward(6*scale)
    qq.begin_fill()
    qq.circle(2)
    qq.end_fill()
    qq.right(8)
    qq.forward(21*scale)
    qq.begin_fill()
    qq.circle(2)
    qq.end_fill()
    qq.setheading(0)  # This is where we finish the drawing and reset the turtle


qq.ht()  # This is needed to hide the pen symbol, so we can see the full drawing

main()  # BEFORE turtle.done() - this is what draws all the code onto the canvas
turtle.done()  # So we can keep the screen open
