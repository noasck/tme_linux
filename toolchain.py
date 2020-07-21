import enum


class Moves(enum.Enum):
    left = -1
    right = 1
    stay = 0

    @staticmethod
    def parse(char):
        moves = {
            "s": Moves.stay,
            "r": Moves.right,
            "*": Moves.stay,
            "l": Moves.left
        }

        return moves[char]


class Result:
    def __init__(self, steps, time, string):
        self._steps = steps
        self._time_elapsed = time
        self._result_str = string

    @property
    def steps(self):
        return self._steps

    @property
    def time_elapsed(self):
        return self._time_elapsed

    @property
    def res_str(self):
        return self._result_str

