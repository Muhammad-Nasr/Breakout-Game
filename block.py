from turtle import Turtle
from random import random


## CONSTANTS

SHAPE = 'square'
STRETCH_WIDTH = 2
STRETCH_LEN = 4
SPACE_X= -85
SPACE_Y = 45


# BLOCKS LEVEL 1
COLOR = 'green'
LEVEL1_X = 350
LEVEL1_Y = -70

## BLOCKS LEVEL 2
COLOR2 = 'orange'
LEVEL2_X = 350
LEVEL2_Y = -25

## BLOCKS LEVEL 3
COLOR3= 'purple'
LEVEL3_X = 350
LEVEL3_Y = 20

## BLOCKS LEVEL 4
COLOR4 = 'blue'
LEVEL4_X = 350
LEVEL4_Y = 65




class Blocks:
    def __init__(self):


        self.all_blocks = []
        self.x1 = LEVEL1_X
        self.x2 = LEVEL2_X
        self.x3 = LEVEL3_X
        self.x4 = LEVEL4_X


    def create_blocks(self):

        for i in range(0, 9):
            self.block = Turtle()
            self.block.shape(SHAPE)
            self.block.penup()
            self.block.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_LEN)

            self.block.color(COLOR)

            self.block.goto(x=self.x1, y=LEVEL1_Y)
            self.all_blocks.append(self.block)
            self.x1 += SPACE_X

        for i in range(0, 9):
            self.block = Turtle()
            self.block.shape(SHAPE)
            self.block.penup()
            self.block.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_LEN)

            self.block.color(COLOR2)

            self.block.goto(x=self.x2, y= LEVEL2_Y)
            self.all_blocks.append(self.block)
            self.x2 += SPACE_X

        for i in range(0, 9):
            self.block = Turtle()
            self.block.shape(SHAPE)
            self.block.penup()
            self.block.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_LEN)

            self.block.color(COLOR3)

            self.block.goto(x= self.x3 ,y= LEVEL3_Y )
            self.all_blocks.append(self.block)

            self.x3 += SPACE_X

        for i in range(0, 9):
            self.block = Turtle()
            self.block.shape(SHAPE)
            self.block.penup()
            self.block.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_LEN)

            self.block.color(COLOR4)

            self.block.goto(x=self.x4, y=LEVEL4_Y)
            self.all_blocks.append(self.block)

            self.x4 += SPACE_X


















