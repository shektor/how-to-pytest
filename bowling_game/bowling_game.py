
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
                score += self.ALL_PINS + self._strike_bonus(frame_index)
                frame_index += 1
                continue

            if self._is_spare(frame_index):
                score += self.ALL_PINS + self._spare_bonus(frame_index)
            else:
                score += self._sum_of_rolls_in_frame(frame_index)
            frame_index += 2

        return score

    def _sum_of_rolls_in_frame(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1]

    def _is_spare(self, frame_index):
        no_of_pins = self._sum_of_rolls_in_frame(frame_index)

        return no_of_pins == self.ALL_PINS

    def _spare_bonus(self, frame_index):
        return self.rolls[frame_index + 2]

    def _is_strike(self, frame_index):
        return self.rolls[frame_index] == self.ALL_PINS

    def _strike_bonus(self, frame_index):
        return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]
