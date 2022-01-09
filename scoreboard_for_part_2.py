from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 14, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("White")
        self.score_board()

    def score_board(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGN, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGN, font=FONT)
        self.goto(0, -30)
        self.write(f"Score: {self.score}", move=False, align=ALIGN, font=FONT)


    def count_score(self):
        self.score += 1
        self.clear()
        self.score_board()

