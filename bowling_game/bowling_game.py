
class Game:

    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def final_score(self):
        score = 0
        roll = 0
        for frame in range(10):
            if self.rolls[roll] + self.rolls[roll + 1] == 10:
                score += 10 + self.rolls[roll + 2]
            else:
                score += self.rolls[roll] + self.rolls[roll + 1]
            roll += 2

        return score
