import turtle as t
from paddle_bar import Paddle
from circle import Ball
import time
from scoreboard import Scoreboard

# Set up the screen
screen = t.Screen()
screen.bgcolor("black")  # Changed to black for classic Pong feel, adjust as you like
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

# Initialize game objects
ball = Ball(0)
paddle1 = Paddle(350)   # Right paddle
paddle2 = Paddle(-350)  # Left paddle
score = Scoreboard()

# Set up key bindings
screen.listen()
screen.onkeypress(paddle1.move_up, "Up")
screen.onkeypress(paddle1.move_down, "Down")
screen.onkeypress(paddle2.move_up, "w")
screen.onkeypress(paddle2.move_down, "s")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.05)  # Smoother and slightly faster
    screen.update()
    ball.move()

    # Bounce off top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Bounce off paddles
    if (ball.distance(paddle1) < 50 and ball.xcor() > 320) or (ball.distance(paddle2) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Right side missed
    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.bounce_x()
        score.l_point()

    # Left side missed
    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.bounce_x()
        score.r_point()

    # Check for winner
    if score.l_score == score.winner_score:
        # time.sleep(1)
        score.goto(0, 0)
        
        score.write("Left Player Wins! Game Over!", align="center", font=("Courier", 30, "normal"))
        game_is_on = False
        # score.reset()
    elif score.r_score == score.winner_score:
        score.goto(0, 0)
        score.write("Right Player Wins! Game Over!", align="center", font=("Courier", 30, "normal"))
        game_is_on = False
        # time.sleep(2)
        # score.reset()

# Close the game
screen.exitonclick()
t.mainloop()



