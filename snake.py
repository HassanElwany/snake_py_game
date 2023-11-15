from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20,0),(-40,0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.items = []
        self.create_snake()
        self.head = self.items[0]
        self.tail = self.items[-1]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segmant(position)
           
    
    def add_segmant(self, position):
            item = Turtle("square")
            item.color("white")
            item.penup()
            item.goto(position)
            self.items.append(item)
    

    def extend_snake(self):
        self.add_segmant(self.items[-1].position())



    def move(self):
        for i in range(len(self.items) - 1, 0, -1):
            new_x = self.items[i - 1].xcor()
            new_y = self.items[i - 1].ycor()
            self.items[i].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)  # Move the head of the snake forward
    

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)