
class Game:

    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def final_score(self):
        score = 0
        for roll in self.rolls:
            score += roll

        return score
