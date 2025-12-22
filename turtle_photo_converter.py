# turtle_photo_converter.py: load a local image into the program to redraw it with turtle

import turtle
from PIL import Image  # pip install Pillow if you don't have it already

# Here we load an image into a variable
img = Image.open("folder/file.png").convert("L")  # Open parameter = file location + "L" for grayscale
img = img.resize((100, 100))  # We should keep the image small or else it might take all day

# Here we create a variable that processes the pixels of the image
pixels = img.load()
width, height = img.size  # These are the parameters made for the image size - x and y

# Create the canvas for the turtle to draw on
screen = turtle.Screen()
t = turtle.Turtle()  # Make the turtle as "t"
t.speed(0)
t.penup()  # Good habit of doing to make sure there's no unwanted lines

# Draw pixels
for y in range(height):  # We first use the y plane as the loop foundation
    for x in range(width):  # Then we layer the x plane onto the y
        brightness = pixels[x, y]  # Resolution variable
        if brightness < 128:  # Threshold for resolution
            t.goto(x - width//2, height//2 - y)  # Resets after each line is completed
            t.dot(2)  # We use dots like pixels with this - the parameter is the size of that dot

t.hideturtle()  # Hide the turtle so we can see our masterpiece
turtle.done()  # Tells the program to keep the window open
