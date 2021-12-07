import numpy as np


def parse_input(data: list[str]) -> np.array:
    return np.array([list(line) for line in data], int)




if __name__ == '__main__':
    from aocd.models import Puzzle
    puzzle = Puzzle(year=2021, day=4)

    report = parse_input(puzzle.input_data.splitlines())
