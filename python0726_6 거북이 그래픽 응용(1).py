import turtle as t

hw = t.Turtle()
hw.shape('turtle')
hw.color('green')

hw.fd(100)
hw.lt(90)
hw.fd(50)

hw.goto(-60, -60)

x = hw.pos()
print(x, hw.xcor(), hw.ycor())
print(hw.distance(0, 0), hw.heading())

hw.seth(180)

hw.home()

print(hw.heading())
