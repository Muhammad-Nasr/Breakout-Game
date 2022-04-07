from turtle import Turtle

#CONSTANTS

COLOR = 'red'
X = 140
Y = -239.2
SPEED = .1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color(COLOR)
        self.speed(SPEED)
        self.goto(x=X, y=Y)
        self.x = 10
        self.y = 10

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)


    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1

    def reset(self):
        self.goto(140, -239)
        self.bounce_y()



