from turtle import Turtle



class Box(Turtle):
    def __init__(self, position, color, ):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.right(90)
        self.penup()
        self.goto(position)
        
    def disappear(self):
        self.ht()
        
    