from turtle import Turtle
FONT = ("Courier", 30, "normal")


class Score(Turtle):
    def __init__(self, a):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        self.score_count(a)

    def score_count(self, a):
        self.clear()
        self.write(arg=f" {self.score} ", align=a, font=FONT)
        self.score += 1


class MidLine(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        # self.shape("square")
        # self.shapesize(stretch_len=0.5, stretch_wid=3)
        self.penup()
        y = 300
        self.goto(0, y)
        self.right(90)
        self.pensize(10)
        self.color("white")
        while y > -440:
            self.pendown()
            self.forward(40)
            self.penup()
            self.forward(20)
            y -= 80
