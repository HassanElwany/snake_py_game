from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #check the collision between food and snake
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        score.increase_score()
    
    #detect collision to the wall
    if snake.head.xcor() > 600 or snake.head.xcor() < -600 or snake.head.ycor() > 600 or snake.head.ycor() < -600:
        game_is_on = False
        score.game_over()

    #detect collision with tail
    for item in snake.items[1:]:
       
        if snake.head.distance(item) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()