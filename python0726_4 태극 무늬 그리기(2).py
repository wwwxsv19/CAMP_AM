import turtle as t

x = 0
win = t.Screen()
win.setup(600, 600)

t.bgcolor('black')
t.shape('turtle')
t.color('red')
t.speed(0)

for i in range(1, 1000):
    if i %3==0: t.color('red')
    elif i%3==1: t.color('blue')
    else: t.color('yellow')
    t.forward(x)
    t.left(230)
    x+=6

win.exitonclick()
