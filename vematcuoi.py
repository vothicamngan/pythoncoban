import turtle
#define pen size
turtle.pensize(5) 
 
#define pen color
turtle.pencolor("Blue") 

#for outer bigger circle
facesize = 200
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.circle(facesize)