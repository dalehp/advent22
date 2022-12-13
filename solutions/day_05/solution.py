from dataclasses import dataclass
from typing import Callable

FILE = "solutions/day_05/input.txt"
TEST_FILE = "solutions/day_05/test_input.txt"


@dataclass
class Instruction:
    quantity: int
    from_stack: int
    to_stack: int


Stack = list[list[str]]


def get_stacks_and_instructions() -> tuple[list[Stack], list[Instruction]]:
    with open(FILE) as f:
        raw_stacks = []
        while s := f.readline().rstrip():
            raw_stacks.append(s)

        raw_instructions = []
        for l in f:
            raw_instructions.append(l.rstrip())

    num_stacks = int(raw_stacks[-1][-1])
    # initialise with dummy 0th entry to make it '1' indexed
    stacks = [[] for _ in range(num_stacks + 1)]

    for stack in raw_stacks[:-1]:
        for i, crate in enumerate(stack[1::4], 1):
            if crate.isalpha():
                stacks[i].insert(0, crate)

    instructions: list[Instruction] = []
    for raw_instruction in raw_instructions:
        move, from_to = raw_instruction.split(" from ")
        _, move_str = move.split(" ")
        from_str, to_str = from_to.split(" to ")
        instructions.append(
            Instruction(
                quantity=int(move_str),
                from_stack=int(from_str),
                to_stack=int(to_str),
            )
        )
    return stacks, instructions


def apply_instuction_a(stacks: list[Stack], instruction: Instruction):
    for _ in range(instruction.quantity):
        stacks[instruction.to_stack].append(stacks[instruction.from_stack].pop())


def apply_instuction_b(stacks: list[Stack], instruction: Instruction):
    popped = []
    for _ in range(instruction.quantity):
        popped.append(stacks[instruction.from_stack].pop())
    popped.reverse()
    stacks[instruction.to_stack].extend(popped)


def solve(instruction_fn: Callable[[list[Stack], Instruction], None]):
    stacks, instructions = get_stacks_and_instructions()
    for instruction in instructions:
        instruction_fn(stacks, instruction)
    print("".join((s[-1] for s in stacks[1:])))


def solve_part_a():
    solve(apply_instuction_a)


def solve_part_b():
    solve(apply_instuction_b)


def run():
    solve_part_a()
    solve_part_b()
