from typing import Callable, Iterable, TextIO

FILE = "solutions/day_04/input.txt"
TEST_FILE = "solutions/day_04/test_input.txt"


def contained(min_1: int, max_1: int, min_2: int, max_2: int) -> bool:
    return (min_1 >= min_2 and max_1 <= max_2) or (min_2 >= min_1 and max_2 <= max_1)


def overlaps(min_1: int, max_1: int, min_2: int, max_2: int) -> bool:
    # I have a feeling you can do this in fewer ops
    return (
        (min_1 >= min_2 and min_1 <= max_2)
        or (max_1 >= min_2 and max_1 <= max_2)
        or (min_2 >= min_1 and min_2 <= max_1)
        or (max_2 >= min_1 and max_2 <= max_1)
    )


def yield_elves_from_file(
    f: TextIO,
) -> Iterable[tuple[tuple[int, int], tuple[int, int]]]:
    for line in f:
        elf_1_str, elf_2_str = line.rstrip().split(",")
        elf_1_min, elf_1_max = tuple((int(a) for a in elf_1_str.split("-")))
        elf_2_min, elf_2_max = tuple((int(a) for a in elf_2_str.split("-")))
        yield ((elf_1_min, elf_1_max), (elf_2_min, elf_2_max))


def solve(check_fn: Callable[[int, int, int, int], bool]):
    count = 0
    with open(FILE) as f:
        for elf_1, elf_2 in yield_elves_from_file(f):
            elf_1_min, elf_1_max = elf_1
            elf_2_min, elf_2_max = elf_2
            count += int(check_fn(elf_1_min, elf_1_max, elf_2_min, elf_2_max))
    print(count)


def solve_part_a():
    solve(contained)


def solve_part_b():
    solve(overlaps)


def run():
    solve_part_a()
    solve_part_b()
