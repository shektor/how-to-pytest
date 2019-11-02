
class Game:
    FRAMES_IN_GAME = 10
    ALL_PINS = 10

    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def final_score(self):
        score = 0
        frame_index = 0
        for frame in range(self.FRAMES_IN_GAME):
            if self._is_strike(frame_index):
                score += self.ALL_PINS
                score += self.rolls[frame_index + 1]
                score += self.rolls[frame_index + 2]
                frame_index += 1
                continue

            if self._is_spare(frame_index):
                score += self.ALL_PINS + self.rolls[frame_index + 2]
            else:
                score += self.rolls[frame_index] + self.rolls[frame_index + 1]
            frame_index += 2

        return score

    def _is_spare(self, frame_index):
        no_of_pins = self.rolls[frame_index] + self.rolls[frame_index + 1]

        return no_of_pins == self.ALL_PINS

    def _is_strike(self, frame_index):
        return self.rolls[frame_index] == self.ALL_PINS
