from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
    
    def random_food(self):
        random_position = random.randint(-260, 260)
        x_position = random_position
        y_position = random_position
        position_food = self.goto(x=x_position, y=y_position)