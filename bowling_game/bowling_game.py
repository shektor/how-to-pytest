
class Game:

    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def final_score(self):
        score = 0
        frame_index = 0
        for frame in range(10):
            if self._is_spare(frame_index):
                score += 10 + self.rolls[frame_index + 2]
            else:
                score += self.rolls[frame_index] + self.rolls[frame_index + 1]
            frame_index += 2

        return score

    def _is_spare(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1] == 10
