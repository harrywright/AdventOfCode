def depth_count(data: list[int]) -> int:
    count = 0
    previous, *data = data
    for depth in data:
        if depth > previous:
            count += 1
        previous = depth
    return count


def slide_depth_count(data: list[int]) -> int:
    count = 0
    previous = None
    for i in range(len(data)-2):
        window = data[i] + data[i + 1] + data[i + 2]
        if previous and window > previous:
            count += 1
        previous = window
    return count


if __name__ == '__main__':
    from aocd.models import Puzzle
    puzzle = Puzzle(year=2021, day=1)
    puzzle_input = puzzle.input_data.splitlines()

    # convert input to ints
    puzzle_input = [int(line) for line in puzzle_input]

    print(depth_count(puzzle_input))
    print(slide_depth_count(puzzle_input))
