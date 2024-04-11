import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
my_turtle = turtle.Turtle()
my_turtle.color("black")

# Write "D"
my_turtle.penup()
my_turtle.goto(-50, -30)
my_turtle.pendown()
my_turtle.write("D", font=("Arial", 30, "normal"))

# Write "N"
my_turtle.penup()
my_turtle.goto(0, -30)
my_turtle.pendown()
my_turtle.write("N", font=("Arial", 30, "normal"))

# Write "T"
my_turtle.penup()
my_turtle.goto(50, -30)
my_turtle.pendown()
my_turtle.write("T", font=("Arial", 30, "normal"))

# Hide the turtle object
my_turtle.hideturtle()

# Keep the screen open
turtle.done()