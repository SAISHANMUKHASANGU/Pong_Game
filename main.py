from turtle import Turtle,Screen
from paddles import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

score_l=0
score_r=0


screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("pong")
screen.tracer(0)


paddle_l=Paddle((-350, 0))
paddle_r=Paddle((350, 0))
ball=Ball()
score=Scoreboard()



screen.listen()
screen.onkeypress(paddle_l.go_up,"w")
screen.onkeypress(paddle_l.go_down,"s")
screen.onkeypress(paddle_r.go_up,"Up")
screen.onkeypress(paddle_r.go_down,"Down")

is_game_on=True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #collide with upper  or lower wall
    if ball.ycor()>=280  or ball.ycor()<=-280:
        ball.bounce_y()

    #collide with paddle
    if ball.xcor()>320 and ball.distance(paddle_r)<50 or ball.xcor()<-320 and ball.distance(paddle_l)<50:
        ball.bounce_x()

    #paddle missing ball
    if ball.xcor() > 400 and ball.distance(paddle_r) > 50 :
        score.l_point()
        ball.reset_position()

    if ball.xcor() < -400 and ball.distance(paddle_l) > 50:
        score.r_point()
        ball.reset_position()

screen.exitonclick()