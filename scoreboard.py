from turtle import Turtle

SCORE = 0
LOSS = 3
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.color('white')
        self.hideturtle()
        self.penup()
        self.score = SCORE
        self.loss = LOSS


    def write_loss(self):
        self.goto(-380, 280)
        self.write(self.loss, align='center', font=FONT)

    def write_score(self):
        self.goto(380, 280 )
        self.write(self.loss, align='center', font=FONT)