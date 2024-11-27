#polygon
#importing library
import turtle    
turtle.Screen().bgcolor("purple")
turtle.Screen().setup(400,400)
polygon = turtle.Turtle() #defined variable
turtle.goto(0,0)
num_sides = 6 #variable
side_length = 100
angle = 360.0 / num_sides
#iterate loop for total number of side
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
     
turtle.done()

