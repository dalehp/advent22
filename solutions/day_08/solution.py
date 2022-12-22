import copy

from solutions.common import ULDR, Grid, Point

FILE = "solutions/day_08/input.txt"
TEST_FILE = "solutions/day_08/test_input.txt"

# height, visiblity flag
Tree = tuple[int, bool]


def scenic_score(grid: Grid[int], at: Point) -> int:
    # edges have at least 1 visibility score of 0
    (min_x, min_y), (max_x, max_y) = grid.bounds
    if at.x in (min_x, max_x) or at.y in (min_y, max_y):
        return 0

    at_height = grid[at]
    total_score = 1
    for direction in ULDR:
        score = 0
        current_position = at + direction
        while (current_height := grid.get(current_position)) is not None:
            score += 1
            if current_height >= at_height:
                break
            current_position += direction
        total_score *= score
    return total_score


def solve_part_a():
    with open(FILE) as f:
        grid: Grid[Tree] = Grid.from_file(f, lambda x: (int(x), False))
    _, (max_x, max_y) = grid.bounds

    # TODO: refactor to use ULDR like above
    # Top to bottom
    for i in range(max_x + 1):
        max_height = -1
        for j in range(max_y + 1):
            height, _ = grid[Point(i, j)]
            if height > max_height:
                max_height = height
                grid[Point(i, j)] = (height, True)

    # Left to right
    for j in range(max_y + 1):
        max_height = -1
        for i in range(max_x + 1):
            height, _ = grid[Point(i, j)]
            if height > max_height:
                max_height = height
                grid[Point(i, j)] = (height, True)

    # Bottom to top
    for i in range(max_x + 1):
        max_height = -1
        for j in range(max_y, -1, -1):
            height, _ = grid[Point(i, j)]
            if height > max_height:
                max_height = height
                grid[Point(i, j)] = (height, True)

    # Right to left
    for j in range(max_y + 1):
        max_height = -1
        for i in range(max_x, -1, -1):
            height, _ = grid[Point(i, j)]
            if height > max_height:
                max_height = height
                grid[Point(i, j)] = (height, True)

    visible = sum((1 for _, (_, v) in grid if v))
    print(visible)


def solve_part_b():
    # This is quite slow, can it be sped up with some clever DP?
    highest_score = 0
    with open(FILE) as f:
        grid: Grid[int] = Grid.from_file(f, int)

    for point, _ in grid:
        score = scenic_score(grid, at=point)
        highest_score = max(score, highest_score)
    print(highest_score)


def run():
    solve_part_a()
    solve_part_b()
