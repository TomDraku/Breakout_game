from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.goto(300,250)
        self.write(f"Your score: {self.score}", align="center", font=("Courier", 12, "normal"))
        
    def point(self):
        self.score += 1
        self.update_score()
        
    def game_over(self):
        self.clear()
        self.goto(-50, 200)
        self.write(f"    Game Over!\nYour score is: {self.score}", align="center", font=("Courier", 30))
        