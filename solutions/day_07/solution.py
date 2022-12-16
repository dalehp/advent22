from dataclasses import dataclass
from enum import Enum
from typing import Iterable, Union

FILE = "solutions/day_07/input.txt"
TEST_FILE = "solutions/day_07/test_input.txt"


class Keyword(Enum):
    UP = ".."


File = tuple[int, str]


@dataclass
class Cd:
    to: str


@dataclass
class ListDirectory:
    contents: list[File]


Command = Cd | ListDirectory


@dataclass
class Directory:
    parent: Union["Directory", None] = None
    size: int = 0


def get_commands_from_file():
    with open(FILE) as f:
        commands: list[Command] = []

        # Skip first line, should just be '$ cd /'
        f.readline()

        while l := f.readline().rstrip():
            _, command, *arguments = l.split()

            match (command, arguments):
                case ("cd", [to]):
                    commands.append(Cd(to=to))
                case ("ls", []):
                    contents = []
                    while not (l := f.readline().rstrip()).startswith("$"):
                        if not l:
                            break
                        position = f.tell()
                        size, name = l.split()
                        if size == "dir":
                            # assume we traverse whole file tree so don't care about this
                            continue
                        contents.append((int(size), name))
                    commands.append(ListDirectory(contents=contents))
                    # go back one line
                    f.seek(position)
                case _:
                    raise ValueError(
                        f"unknown command {command} with arguments {arguments}"
                    )
    return commands


def build_file_tree(commands: Iterable[Command]) -> list[Directory]:
    file_tree = [Directory()]
    current_dir = file_tree[0]
    for command in commands:
        match command:
            case ListDirectory(contents=contents):
                contents_size = sum(f_size for f_size, _ in contents)
                current_dir.size += contents_size
                parent_dir = current_dir
                while parent_dir := parent_dir.parent:
                    parent_dir.size += contents_size
            case Cd(to=Keyword.UP.value):
                current_dir = current_dir.parent
            case Cd(to=to):
                current_dir = Directory(parent=current_dir)
                file_tree.append(current_dir)
    return file_tree


def solve_part_a():
    commands = get_commands_from_file()
    tree = build_file_tree(commands)
    big_dir_sum = 0
    for directory in tree:
        if directory.size <= 100000:
            big_dir_sum += directory.size
    print(big_dir_sum)


def solve_part_b():
    commands = get_commands_from_file()
    tree = build_file_tree(commands)
    total_disk_space = 70000000
    needed_disk_space = 30000000
    free_disk_space = total_disk_space - tree[0].size
    required_to_delete = needed_disk_space - free_disk_space

    smallest_dir = float("inf")
    for directory in tree:
        if directory.size >= required_to_delete:
            smallest_dir = min(smallest_dir, directory.size)
    print(smallest_dir)


def run():
    solve_part_a()
    solve_part_b()
