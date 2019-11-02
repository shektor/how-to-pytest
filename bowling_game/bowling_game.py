
class Game:

    def __init__(self):
        self.score = 0

    def roll(self, pins):
        self.score += pins

    def final_score(self):
        return self.score
