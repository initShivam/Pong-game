from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")  # Make sure background color supports this
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0  # ✅ lowercase r
        self.winner_score = 5
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-80, 200)
        self.write(f"{self.l_score}", align="center", font=("Courier", 40, "normal"))
        self.goto(80, 200)
        self.write(f"{self.r_score}", align="center", font=("Courier", 40, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def reset(self):
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 30, "normal"))

    def display_winner(self, winner):
        self.goto(0, 0)
        self.write(f"{winner} Wins!", align="center", font=("Courier", 30, "normal"))
