from turtle import Turtle

MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for pos in range(0,3):
            self.add_seg(pos)
            self.snake[pos].goto((pos*-20), y=0)

    def move_snake(self):
        for block in range(len(self.snake)-1,0,-1):    
            self.snake[block].goto(self.snake[block-1].xcor(), self.snake[block-1].ycor())
        self.snake[0].forward(MOVE_DIST)

    def reset(self):
        for seg in self.snake:
            seg.goto(1000,1000)
        self.snake.clear()
        self.create_snake()

    def add_seg(self, position):
        new_turtle = Turtle(shape='square')
        new_turtle.penup()
        new_turtle.color('white')
        # new_turtle.goto(x=(position*-20), y=0)
        self.snake.append(new_turtle) 

    def extend_snake(self):
        self.add_seg(self.snake[-1])
        self.snake[-1].goto(self.snake[-2].position())

    def up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)

    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)

    def left(self):
        if self.snake[0].heading() != RIGHT:
          self.snake[0].setheading(LEFT)

    def right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)
     


