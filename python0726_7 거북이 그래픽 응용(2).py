import turtle as t

win = t.Screen()

def turn_right():                    
    t.setheading(0)                  
    t.forward(10)           

def turn_up():            
    t.setheading(90)
    t.forward(10)

def turn_left():           
    t.setheading(180)
    t.forward(10)

def turn_down():             
    t.setheading(270)
    t.forward(10)

def pen_down():
     t.down()

def pen_up():
    t.up()

def mousegoto(x,y):
    pos=t.towards(x,y)
    t.setheading(pos)
    t.goto(x,y)

win.onclick(mousegoto)

t.shape("turtle")                          

t.onkeypress(turn_right, "d") 
t.onkeypress(turn_up, "w")
t.onkeypress(turn_left, "a")
t.onkeypress(turn_down, "s")

t.onkeypress(pen_down, "c")
t.onkeypress(pen_up, "v")

t.listen()
win.listen()
t.mainloop()
