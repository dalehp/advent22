from more_itertools import windowed

FILE = "solutions/day_06/input.txt"


def first_marker_index(buffer: str, window_len: int) -> int:
    for i, window in enumerate(windowed(buffer, window_len)):
        if len(set(window)) == window_len:
            return i + window_len


def solve(window_len):
    with open(FILE) as f:
        buffer = f.readline().rstrip()
    print(first_marker_index(buffer, window_len))


def solve_part_a():
    solve(window_len=4)


def solve_part_b():
    solve(window_len=14)


def run():
    solve_part_a()
    solve_part_b()
