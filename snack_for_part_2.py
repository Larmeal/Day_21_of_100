from turtle import Turtle, hideturtle

class Snack:
    def __init__(self):
        self.position_snack = [(0, 0), (-20, 0), (-40, 0)]
        self.segment = []
        self.outline_of_snack()
        self.head_snack = self.segment[0]

    def outline_of_snack(self):
        for position in self.position_snack:
            self.manufacture_snack(position)

    def manufacture_snack(self, position):
        self.snack = Turtle(shape="square")
        self.snack.color("White")
        self.snack.penup()
        self.snack.goto(position)
        self.segment.append(self.snack)

    def extention(self):
        self.manufacture_snack(self.segment[-1].position())

    def hidesnack(self):
        self.snack = hideturtle()

    def move(self):
        for n in range(len(self.segment) - 1, 0, -1):
                position_x = self.segment[n - 1].xcor()
                position_y = self.segment[n -1].ycor()
                self.segment[n].goto(position_x, position_y)
        self.head_snack.forward(20)
        
    def right(self):
        if self.head_snack.heading() != 180:
            self.head_snack.setheading(0)

    def up(self):
        if self.head_snack.heading() != 270:
            self.head_snack.setheading(90)

    def left(self):
        if self.head_snack.heading() != 0:
            self.head_snack.setheading(180)

    def down(self):
        if self.head_snack.heading() != 90:
            self.head_snack.setheading(270)