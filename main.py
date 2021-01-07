from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Setting the turtles animation off on screen.
# We won't be able to see anything move on the canvas
# even when the objects are performing some action in the background.
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    # Since we had turned off the animation (at line 15),
    # Update the screen to show the new position of the snake.
    # Also, screen will be updated when all the segments of snake would have moved forward.
    # Thus, it will look as if the whole snake is moving forward at a time.
    screen.update()

    # Adding a 0.1 seconds delay after all the segments of snake move.
    # This means sleep for 0.1 second before moving the snake again.
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    # Detect collision with tail.
    for segment in snake.snake_segments[1:]:
        # If head collides with any segment in the tail:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
