from turtle import Screen
from turtle import Turtle
import time
from block import Blocks
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard


## todo
screen = Screen()

screen.setup(800, 600)
screen.title('Break Out Game')
screen.tracer(n=0)
screen.bgcolor('black')

##----------------


paddle = Paddle()
ball = Ball()
blocks = Blocks()
blocks.create_blocks()
score_board = ScoreBoard()



## DETECT KET PRESS

screen.listen()
screen.onkey(paddle.move_right, key='Right')
screen.onkey(paddle.move_left, key='Left')


should_continue = True
while should_continue:
    time.sleep(.5)
    screen.update()
    ball.move()


    for block in blocks.all_blocks:

        if ball.distance(block) < 35 :

            ball.bounce_y()
            block.goto(1000, 1000)
            score_board.score += 1


    if ball.ycor() > 290:
        ball.bounce_y()


    elif ball.xcor() > 380 or ball.xcor() < -370:
        ball.bounce_x()

    elif ball.distance(paddle) < 30:
        ball.bounce_y()

    elif 60 > ball.distance(paddle) > 30 and -235 > ball.ycor() > -250:
        ball.bounce_y()
        print(ball.ycor())

    elif ball.ycor() < - 270:
        ball.reset()
        score_board.loss -= 1



    elif blocks.all_blocks == []:
        score_board.write_score()
        should_continue = False



    elif score_board == 0:
        score_board.write_loss()
        should_continue = False
















screen.mainloop()