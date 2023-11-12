from turtle import Screen, Turtle


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

item_1 = Turtle("square")
item_1.color("white")

x = 0
for _ in range(3):
    item_2 = Turtle("square")
    item_2.color("white")
    item_2.goto(x, 0)
    x += -20


screen.exitonclick()