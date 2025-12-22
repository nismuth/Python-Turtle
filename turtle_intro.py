# turtle_intro.py: basic turtle operations and rules

# This is always needed to use the turtle library
import turtle  # This is the full name of the library but...
# ...if you want to make it easier to use try something like: "import turtle as t"

# We're naming the turtle "Leo" and making that the declared variable
leo = turtle.Turtle()  # turtle.Turtle() means that it's creating a Turtle from the turtle library

# Here we customize Leo to how we want it
leo.pencolor('green')  # Use conventional colors or hex #'s - don't forget the #
leo.speed(1)  # The speed range is (0-9), 0 being the quickest and 1 the slowest

# This is how we get to drawing:
leo.penup()  # penup() makes sure the pen "doesn't touch the paper" when moving it
leo.goto(0, 0)  # goto(x, y) moves your pen to a certain spot on the canvas with coordinates
leo.pendown()  # penup() is putting the pen on the paper

# Here we're moving the pen
leo.forward(100)  # This is how you drag your pen to draw lines
leo.left(90)  # This rotates your turtle or imagine your arm shifting - the parameter is the degrees you want to rotate

# Let's complete a square
leo.forward(100)
leo.left(90)
leo.forward(100)
leo.left(90)
leo.forward(100)

# Repeating lines in coding can become annoying to manage so loops can clean it up for us
# Before we do that let's clear our screen with...
turtle.clearscreen()

# clearscreen() removes everything, even your turtle, so you need to remake one when you use it
leo = turtle.Turtle()

leo.pendown()  # Not needed but good to make sure it's down
# A for loop can let us do the same thing but in a more organized fashion
# TODO: square
for i in range(4):  # This loops (repeats) a certain group of commands 4x
    leo.forward(100)
    leo.left(90)

leo.reset()  # This is how we go back to (0, 0)
# Let's try to make a triangle now with what we know
# TODO: triangle
for i in range(3):  # Loop 3x for 3 sides... of course
    leo.forward(100)
    leo.left(120)  # We use the sum of 2 angles of an equilateral triangle

leo.reset()
# We can also make a star with the same principles of a triangle just with every acute angles
# TODO: star
for _ in range(5):  # 5 loops for 5 points
    leo.forward(100)
    leo.right(144)  # This is the angle we use to account for rotating 90 + 54 for a clean star

# You can also use math for your drawing - useful for more intricate projects
# TODO: circle from math
turns = 0  # We create a variable at 0 we can give the loop something to count with
while turns <= 7:  # While the amount of turns is less than or equal to 0 it does the loop
    turns += 1  # Under those circumstances it also adds 1 to the count
    for i in range(turns):  # We use the "turns" variable as a conductor that tells us how long to let the train go
        leo.forward(20)
        leo.right(10)

# This is always needed to keep the turtle window open - it tells the program that you want to see your work
turtle.done()  # Use turtle - not the name you gave it

