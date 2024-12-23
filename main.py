from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score, MidLine
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("The Pong Game!")

screen.tracer(0)
pal = Paddle(370)
pel = Paddle(-370)
screen.listen()
screen.onkey(pal.go_up, "k")
screen.onkey(pal.go_down, "m")
screen.onkey(pel.go_up, "a")
screen.onkey(pel.go_down, "z")

ball = Ball()
l_score = Score("right")
r_score = Score("left")

midline = MidLine()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # detection of collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.col()
    # detection of collision with paddle
    if ball.distance(pal) < 50 and ball.xcor() > 320 or ball.distance(pel) < 50 and ball.xcor() < -320:
        ball.bounce()
    elif ball.distance(pal) > 50 and ball.xcor() > 350:
        l_score.score_count("right")
        time.sleep(0.2)
        ball.home()
        ball.bounce()
    elif ball.distance(pel) > 50 and ball.xcor() < -350:
        r_score.score_count("left")
        time.sleep(0.2)
        ball.home()
        ball.bounce()
screen.exitonclick()
