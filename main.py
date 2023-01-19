from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="d", fun=snake.right)

game_is_on = True

while game_is_on:
    screen.update()
    score.current_score()
    time.sleep(0.1)

    snake.move_snake()

    if snake.snake[0].distance(food) < 15:
        food.random_loc()
        snake.extend_snake()
        # score.score += 1
        score.increase_score()

    if snake.snake[0].xcor() > 290 or snake.snake[0].xcor() < -290 or snake.snake[0].ycor() > 290 or snake.snake[0].ycor() < -290:
        # game_is_on = False
        score.reset()
        snake.reset()
        # score.game_end()

    for seg in snake.snake[1:]:
        # if snake.snake[0] == seg:
        #     pass
        if snake.snake[0].distance(seg) < 15:
            # game_is_on = False
            score.reset()
            snake.reset()
            # score.game_end()

screen.exitonclick()