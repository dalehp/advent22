FILE = "solutions/day_01/input.txt"
TEST_FILE = "solutions/day_01/test_input.txt"


def add_into_top_3(top3: list[int], item: int) -> list[int]:
    if len(top3) < 3:
        return sorted([*top3, item])
    if item < top3[0]:
        return top3
    return sorted([*top3[1:], item])


def solve_part_b():
    top_3_calories: list[int] = []
    calorie_count = 0
    with open(FILE) as f:
        for line in f:
            if not line.rstrip():
                top_3_calories = add_into_top_3(top_3_calories, calorie_count)
                calorie_count = 0
                continue
            calorie_count += int(line.rstrip())
    top_3_calories = add_into_top_3(top_3_calories, calorie_count)
    print(sum(top_3_calories))


def solve_part_a():
    most_calories = 0
    calorie_count = 0
    with open(FILE) as f:
        for line in f:
            if not line.rstrip():
                most_calories = max(most_calories, calorie_count)
                calorie_count = 0
                continue
            calorie_count += int(line.rstrip())
    most_calories = max(most_calories, calorie_count)
    print(most_calories)


def run():
    solve_part_a()
    solve_part_b()
