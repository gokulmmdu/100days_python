from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0 , 270)
        self.color('white')
        self.write(f'score:{self.score}',align='center',font=('Arial',15,'bold'))
        self.ht()

    def game_over(self):

        self.goto(0,0)
        self.write(f'Game over',align='center',font=('Arial',15,'bold'))




    def increse_score(self):
        self.score += 1
        self.clear()
        self.write(f'score:{self.score}',align='center',font=('Arial',15,'bold'))    