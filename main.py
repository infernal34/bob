import turtle
# Function to draw a circle with a specified color
def draw_circle(color, radius):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Function to draw a rectangle with a specified color
def draw_rectangle(color, width, height):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

# Function to draw a face based on user inputs
def draw_face():
    # Gather user inputs
    eye_color = input("Enter eye color 1=brown 2=green 3=blue ")
    skin_color = input("Enter skin color 1-brown 2=white 3=black ")
    hair_color = input("Enter hair color 1=brown 2=yellow 3=black 4=red ")
    has_beard = input("Do you want a beard? (yes/no): ").lower() == "yes"
    has_mustache = input("Do you want a mustache? (yes/no): ").lower() == "yes"
    hair_style = input("Enter hair style 1=short 2=long 3=curly 4=shiny ")

    # Set up Turtle
    turtle.speed(2)
    turtle.hideturtle()
    turtle.bgcolor("white")

    # Draw face
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    if skin_color == 1:
      turtle.color('#96610c')

    # Draw eyes
    turtle.penup()
    turtle.goto(-50, 50)
    turtle.pendown()
    draw_circle(eye_color, 25)

    turtle.penup()
    turtle.goto(50, 50)
    turtle.pendown()
    draw_circle(eye_color, 25)

    # Draw mouth
    turtle.penup()
    turtle.goto(-50, -50)
    turtle.pendown()
    draw_rectangle("black", 100, 20)

    # Draw beard if requested
    if has_beard:
        turtle.penup()
        turtle.goto(-50, -70)
        turtle.pendown()
        draw_rectangle("brown", 100, 20)

    # Draw mustache if requested
    if has_mustache:
        turtle.penup()
        turtle.goto(-25, 20)
        turtle.pendown()
        draw_rectangle("black", 50, 10)

    # Draw hair
    turtle.penup()
    turtle.goto(-100, 120)
    turtle.pendown()
    if hair_style == 1:
        draw_circle(hair,  )
    
    # Display hair style
    turtle.penup()
    turtle.goto(-60, 180)
    turtle.pendown()
    turtle.write("Hair: {hair_style}", font=("Arial", 12, "normal"))

draw_face()