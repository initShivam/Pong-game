import turtle as t

class Ball(t.Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.speed_ball = 0.1
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.x_move = 10
        self.y_move = 10


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.speed_ball *= 0.9
     
    def bounce_x(self):
        self.x_move *= -1
    
    def reset(self):
        self.goto(0,0)
        self.speed_ball = 0.1
        self.bounce_x()