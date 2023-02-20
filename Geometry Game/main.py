from turtle import Turtle,Screen
import turtle
from rectangle import *

myturtle = Turtle(visible=False)
point1, point2, point3, point4 = create_points_2()
var = f"Co-Ordinates : {point1.get_point()}, {point2.get_point()}, {point3.get_point()}, {point4.get_point()}"
rect = GUIRectangle(point1, point2, point3, point4)
rect.draw(myturtle)
myturtle.penup()
myturtle.setposition(-40, -40)
myturtle.write(var)
myturtle.pendown()
turtle.done()

