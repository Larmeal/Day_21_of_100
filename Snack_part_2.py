from turtle import Screen
from snack_for_part_2 import Snack
from food_for_part_2 import Food
from scoreboard_for_part_2 import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The snack game")
screen.tracer(0)
screen.listen()

snack = Snack()
screen.onkey(snack.up, key="Up")
screen.onkey(snack.down, key="Down")
screen.onkey(snack.left, key="Left")
screen.onkey(snack.right, key="Right")

food = Food()
score = Scoreboard()

again = True
while again:
    screen.delay(0)
    screen.update()
    time.sleep(0.1)
    snack.move()

    if snack.head_snack.distance(food) < 15:
        food.random_food()
        snack.extention()
        score.count_score()

    if snack.head_snack.xcor() < -290 or snack.head_snack.xcor() > 290 or snack.head_snack.ycor() < -290 or snack.head_snack.ycor() > 290:
        again = False
        score.game_over()

    for segment in snack.segment[1:]:
        if snack.head_snack.distance(segment) < 10:
            again = False
            score.game_over()

screen.exitonclick()