from turtle import Turtle

# CONSTANTS
COLOR = 'white'
SHAPE = 'square'
STRETCH_WIDTH = 1
STRETCH_LEN = 9
X = 0
Y = -250
SPACE = 20
END_RIGHT = 300
END_LEFT = -308



class Paddle(Turtle):
    def __init__(self):
        super().__init__()

        self.shape(SHAPE)
        self.penup()
        self.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_LEN)
        self.color(COLOR)
        self.goto(x=X, y=Y)

    def move_right(self):
        if self.xcor() < END_RIGHT:
            self.forward(SPACE)


    def move_left(self):
        if self.xcor() > END_LEFT:
            self.backward(SPACE)
