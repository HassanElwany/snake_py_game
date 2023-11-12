from turtle import Screen, Turtle
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


x = 0

items = []
for _ in range(3):
    item_1 = Turtle("square")
    item_1.color("white")
    item_1.penup()
    item_1.goto(x, 0)
    x += -20
    items.append(item_1)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    for item in range(2, 0, -1):
        
        





screen.exitonclick()