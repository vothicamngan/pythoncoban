import turtle

t = turtle.Turtle()
def rectangle(hor,ver,col):
    t.pendown() #tạo con trỏ
    t.pensize(1)
    t.color(col)
    t.begin_fill()
    for counter in range(1,3):
        t.forward(hor)
        t.right(90)
        t.forward(ver)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.speed('slow')
turtle.bgcolor('white')
t.goto(300,-350)
rectangle(50,20,'blue')
