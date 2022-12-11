from more_itertools import chunked

FILE = "solutions/day_03/input.txt"
TEST_FILE = "solutions/day_03/test_input.txt"


def priority(character: str) -> int:
    if len(character) != 1:
        raise ValueError(f"{character} is not a character")

    if character.islower():
        return ord(character) - ord("a") + 1
    if character.isupper():
        return ord(character) - ord("A") + 27

    raise ValueError(f"{character} is not a letter")


def solve_part_a():
    with open(FILE) as f:
        sum_priorities = 0
        for line in f:
            rucksacks = line.rstrip()
            rucksack_1 = set(rucksacks[: len(rucksacks) // 2])
            rucksack_2 = set(rucksacks[len(rucksacks) // 2 :])

            [common_item] = rucksack_1 & rucksack_2

            sum_priorities += priority(common_item)
    print(sum_priorities)


def solve_part_b():
    with open(FILE) as f:
        rucksacks = [set(line.rstrip()) for line in f]

    elves = chunked(rucksacks, 3)

    sum_priorities = 0
    for elf in elves:
        [common_item] = elf[0] & elf[1] & elf[2]
        sum_priorities += priority(common_item)

    print(sum_priorities)


def run():
    solve_part_a()
    solve_part_b()
