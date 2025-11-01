from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake_game\data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(arg=f"Score: {self.score}, High score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake_game\data.txt", mode="w") as file:
                score = str(self.score)
                file.write(score)
        self.score = 0
        self.update_scoreboard()

    def inscrease_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}, High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game over", align=ALIGNMENT, font=FONT)

