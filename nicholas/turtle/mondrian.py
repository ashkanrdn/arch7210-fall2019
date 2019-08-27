import turtle

class Mondrian(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        screen = self.getscreen()
        self.width = screen.window_width()
        self.height = screen.window_height()
    
    def toX(self, position):
        return (position - 0.5) * self.width
    
    def toY(self, position):
        return (position - 0.5) * self.height

    def moveTo(self, x, y):
        self.penup()
        self.goto(x, y)
        self.pendown()

    def line(self, x1, y1, x2, y2, width=20):
        self.moveTo(self.toX(x1), self.toY(y1))
        self.pensize(width)
        self.goto(self.toX(x2), self.toY(y2))

    def rect(self, x1, y1, x2, y2, fillcolor):
        self.moveTo(self.toX(x1), self.toY(y1))
        self.pensize(0)
        self.fillcolor(fillcolor)
        self.begin_fill()
        self.goto(self.toX(x1), self.toY(y2))
        self.goto(self.toX(x2), self.toY(y2))
        self.goto(self.toX(x2), self.toY(y1))
        self.goto(self.toX(x1), self.toY(y1))
        self.end_fill()



m = Mondrian()
m.hideturtle()
m.speed(0)

m.rect(0.25, 0.25, 1, 1, '#ff2020')
m.rect(0, 0, 0.25, 0.25, '#3366ff')
m.rect(0.875, 0, 1, 0.125, '#ffcc33')

m.line(0.25, 0, 0.25, 1)
m.line(0, 0.25, 1, 0.25)
m.line(0, 0.625, 0.25, 0.625)
m.line(0.875, 0, 0.875, 0.25)
m.line(0.875, 0.125, 1, 0.125)

turtle.done()