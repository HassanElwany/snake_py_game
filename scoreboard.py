from turtle import Turtle


class Score(Turtle):
   
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 600)
        self.hideturtle()
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 26, "normal"))
    

    def game_over(self):
        self.clear()
        self.write(f"Game is Over", False, align="center", font=("Arial", 26, "normal"))
    

    def increase_score(self):

        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 26, "normal"))
        


    