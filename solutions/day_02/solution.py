from enum import Enum
from typing import TextIO

FILE = "solutions/day_02/input.txt"
TEST_FILE = "solutions/day_02/test_input.txt"


class Result(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __lt__(self, o: "RPS") -> bool:
        return (self.value + 1) % 3 == o.value % 3

    def plays(self, o: "RPS") -> Result:
        if self > o:
            return Result.WIN
        elif self == o:
            return Result.DRAW
        return Result.LOSE

    def score(self, o: "RPS") -> int:
        result = self.plays(o)
        return result.value + self.value

    def for_result(self, result: Result) -> "RPS":
        """If you are playing against this, returns the move you
        must play to achieve the given result.
        """
        if result == Result.DRAW:
            return self
        elif result == Result.WIN:
            return RPS((self.value % 3) + 1)
        return RPS((self.value - 2) % 3 + 1)


OPPONENT_ALIASES: dict[str, RPS] = {"A": RPS.ROCK, "B": RPS.PAPER, "C": RPS.SCISSORS}

YOU_ALIASES: dict[str, RPS] = {
    "X": RPS.ROCK,
    "Y": RPS.PAPER,
    "Z": RPS.SCISSORS,
}

RESULT_ALIASES: dict[str, Result] = {
    "X": Result.LOSE,
    "Y": Result.DRAW,
    "Z": Result.WIN,
}


def yield_rps_from_file(f: TextIO) -> tuple[RPS, RPS]:
    for line in f:
        a, b = line.rstrip().split()
        yield OPPONENT_ALIASES[a], YOU_ALIASES[b]


def yield_rps_result_from_file(f: TextIO) -> tuple[RPS, Result]:
    for line in f:
        a, b = line.rstrip().split()
        yield OPPONENT_ALIASES[a], RESULT_ALIASES[b]


def solve_part_a():
    with open(FILE) as f:
        scores = (you.score(opp) for opp, you in yield_rps_from_file(f))
        print(sum(scores))


def solve_part_b():
    with open(FILE) as f:
        scores = []
        for opp, res in yield_rps_result_from_file(f):
            you = opp.for_result(res)
            scores.append(you.score(opp))
        print(sum(scores))


def run():
    solve_part_a()
    solve_part_b()
