from .solution import RPS, Result


def test_rps():
    assert RPS.ROCK.plays(RPS.SCISSORS) == Result.WIN
    assert RPS.ROCK.plays(RPS.ROCK) == Result.DRAW
    assert RPS.ROCK.plays(RPS.PAPER) == Result.LOSE

    assert RPS.PAPER.plays(RPS.ROCK) == Result.WIN
    assert RPS.PAPER.plays(RPS.PAPER) == Result.DRAW
    assert RPS.PAPER.plays(RPS.SCISSORS) == Result.LOSE

    assert RPS.SCISSORS.plays(RPS.PAPER) == Result.WIN
    assert RPS.SCISSORS.plays(RPS.SCISSORS) == Result.DRAW
    assert RPS.SCISSORS.plays(RPS.ROCK) == Result.LOSE


def test_rps_scores():
    assert RPS.PAPER.score(RPS.ROCK) == 8
    assert RPS.ROCK.score(RPS.PAPER) == 1
    assert RPS.SCISSORS.score(RPS.SCISSORS) == 6


def test_rps_result():
    assert RPS.ROCK.for_result(Result.WIN) == RPS.PAPER
    assert RPS.ROCK.for_result(Result.DRAW) == RPS.ROCK
    assert RPS.ROCK.for_result(Result.LOSE) == RPS.SCISSORS

    assert RPS.PAPER.for_result(Result.WIN) == RPS.SCISSORS
    assert RPS.PAPER.for_result(Result.DRAW) == RPS.PAPER
    assert RPS.PAPER.for_result(Result.LOSE) == RPS.ROCK

    assert RPS.SCISSORS.for_result(Result.WIN) == RPS.ROCK
    assert RPS.SCISSORS.for_result(Result.DRAW) == RPS.SCISSORS
    assert RPS.SCISSORS.for_result(Result.LOSE) == RPS.PAPER
