from turtle import Turtle

FONT=('courier', 10, 'normal')
ALIGNMENT = 'center'

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        # self.high_score = 0
        with open(file="data.txt", mode='r') as file:
            self.high_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.goto(0,280)
        self.current_score()

    def current_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file="data.txt", mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0

    def increase_score(self):
        self.score += 1
        self.current_score()

    # def game_end(self):
    #     self.goto(0,0)
    #     self.write(arg="Game Over!", align=ALIGNMENT, font=FONT)