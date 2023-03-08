import turtle
import interface_paint
def clear():
    pen.clear()
def penred():
    pen.color('red')
def penblue():
    pen.color('blue')
def pengreen():
    pen.color('green')
def penyellow():
    pen.color('yellow')
def moveUp():
    x = pen.position()[0]
    y = pen.position()[1]
    pen.setposition(x, y+5)
def moveDown():
    x, y = pen.position()
    pen.setposition(x, y-5)
def moveRight():
    x, y = pen.position()
    pen.setposition(x+5, y)
def moveLeft():
    x, y = pen.position()
    pen.setposition(x-5, y)
def draw(x, y):
    pen.ondrag(None)
    pen.goto(x, y)
    pen.setheading(turtle.towards(x, y))
    pen.ondrag(draw)
def change():
    if pen.isvisible():
        pen.up()
        pen.hideturtle()
    else:
        pen.down()
        pen.showturtle()
pen = turtle.Turtle()
pen.speed(10)
pen.shape('circle')
pen.pensize(4)
pen.ondrag(draw)
sc = turtle.Screen()
sc.setup(1280, 720)
sc.onkey(moveUp, 'Up')
sc.onkey(moveDown, 'Down')
sc.onkey(moveRight, 'Right')
sc.onkey(moveLeft, 'Left')
sc.onkey(change, 'space')
sc.onkey(pengreen, 'g')
sc.onkey(penblue, 'b')
sc.onkey(pengreen, 'G')
sc.onkey(penblue, 'B')
sc.onkey(penred, 'R')
sc.onkey(penred, 'r')
sc.onkey(clear, 'c')
sc.onkey(clear, 'C')
turtle.hideturtle()
sc.listen()
sc.mainloop()