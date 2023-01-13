from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 4
        self.y_move = 4
        self.move_speed = 4.0
        
    def move(self):
        new_x = self.x_move + self.xcor()
        new_y = self.y_move + self.ycor()
        self.goto(new_x, new_y)
        
    def bounce_y(self):
        self.y_move *=-1
        self.move_speed *= 1.2
        
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 1.2
    
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_y()
    
        
        
        
    
    