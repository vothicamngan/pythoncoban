import turtle
import random
t = turtle.Turtle()
r=70
tt= 20
i =1

while i<=50:
    t.right(tt)
    for loop in range(2):
        t.circle(r,90)
        t.circle(r/2,90)
        tt += 1
t.mainloop()
