import turtle
turtle.colormode(255)
def hinh_tam_giac(x,y,d):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(1,4):
        turtle.left(120)
        turtle.forward(d)
    turtle.penup()
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
x = -210
y = 50
d = 60
for j in range(1,4):
    hinh_tam_giac(x,y,d)
    y -=d
    d += 10
turtle.goto(x*1.27,-d+10)
turtle.pendown()
hinh_chu_nhat(30,70)
turtle.goto(-150,0)
turtle.pendown()
hinh_chu_nhat(250,170)
turtle.goto(-55,-70)
turtle.pendown()
hinh_chu_nhat(70,100)
turtle.pendown()
hinh_tam_giac(100,0,250)
   

x1 = 250
y1= 50
d1 = 70 
for j in range(1,4):
    hinh_tam_giac(x1,y1,d1)
    y1 -=d1
    d1 += 10
turtle.goto(x1/1.3,-d1)
turtle.pendown()
hinh_chu_nhat(30,70)
turtle.mainloop()
