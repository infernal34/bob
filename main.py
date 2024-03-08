import turtle
def draw_face(hair_color, eye_color, skin_color, beard_style, mustache_style):
   turtle.speed(2)
   # Draw head
   turtle.color(skin_color)
   turtle.begin_fill()
   turtle.circle(100)
   turtle.end_fill()
   # Draw eyes
   turtle.penup()
   turtle.goto(-40, 120)
   turtle.pendown()
   turtle.color(eye_color)
   turtle.begin_fill()
   turtle.circle(15)
   turtle.end_fill()
   turtle.penup()
   turtle.goto(40, 120)
   turtle.pendown()
   turtle.color(eye_color)
   turtle.begin_fill()
   turtle.circle(15)
   turtle.end_fill()
   # Draw beard
   turtle.penup()
   turtle.goto(0, 60)
   turtle.pendown()
   turtle.width(5)
   turtle.color(hair_color)
   if beard_style == "full":
       turtle.circle(30, 180)
   elif beard_style == "goatee":
       turtle.goto(-15, 60)
       turtle.circle(15, 180)
   # Draw mustache
   turtle.penup()
   turtle.goto(-20, 90)
   turtle.pendown()
   if mustache_style == "normal":
       turtle.goto(-40, 80)
       turtle.width(3)
       turtle.forward(40)
   elif mustache_style == "handlebar":
       turtle.goto(-35, 85)
       turtle.width(3)
       turtle.circle(15, 180)
   turtle.hideturtle()
   turtle.done()
# Example usage
hair_color = input("Enter hair color: ")
eye_color = input("Enter eye color: ")
skin_color = input("Enter skin color: ")
beard_style = input("Enter beard style (full/goatee): ")
mustache_style = input("Enter mustache style (normal/handlebar): ")
draw_face(hair_color, eye_color, skin_color, beard_style, mustache_style)            
