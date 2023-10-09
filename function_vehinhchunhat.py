import turtle
turtle.colormode(255)
def hinh_chu_nhat(d1,d2):
    i =1
    turtle.color(200,100,150)
    while i <3:
        turtle.forward(d1)
        turtle.right(90)
        turtle.forward(d2)
        turtle.right(90)
        i +=1
    turtle.penup()
j = 1
x1 = -200
x2 = -200
for i in (1,2):
    
    turtle.penup()
    turtle.goto(x1,100)
    turtle.pendown()
    hinh_chu_nhat(90,110)
    x1 += 90
for i in (1,2):
    turtle.penup()
    turtle.goto(x2,210)
    turtle.pendown()
    hinh_chu_nhat(90,110)
    x2 += 90
x3 = -80
x4 = -80
for i in (1,2):
    
    turtle.penup()
    turtle.goto(x3,75)
    turtle.pendown()
    hinh_chu_nhat(30,50)
    x3 -=90
for i in (1,2):
    turtle.penup()
    turtle.goto(x4,185)
    turtle.pendown()
    hinh_chu_nhat(30,50)
    x4 -=90
turtle.penup()   
turtle.goto(-20,160)
turtle.pendown()
hinh_chu_nhat(150,170)
x5= 6

for i in (1,2):
    turtle.penup()
    turtle.goto(x5,60)
    turtle.pendown()
    hinh_chu_nhat(50,70)
    x5 +=50

# for i in (1,2):
#     turtle.penup()
#     turtle.goto(x2/2,y2/2)
#     turtle.pendown()
#     hinh_chu_nhat()
#     x2 += 90
    # /
    # turtle.penup()
    # turtle.goto(-200,100)
    # turtle.pendown()
    # hinh_chu_nhat()
    # turtle.penup()
    # turtle.goto(-110,100)
    # turtle.pendown()
    # hinh_chu_nhat()
    # turtle.penup()
    # turtle.goto(-200,210)
    # turtle.pendown()
    # hinh_chu_nhat()
    # turtle.goto(-110,210)
    # turtle.pendown()
    # hinh_chu_nhat()
    # turtle.penup()
turtle.mainloop()
