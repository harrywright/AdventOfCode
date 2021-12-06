def parse_input(data):
    horizontal = 0
    vertical = 0
    for line in data:
        command, count = line.split()
        if command == 'forward':
            horizontal += int(count)
        if command == 'up':
            vertical -= int(count)
        if command == 'down':
            vertical += int(count)
    return horizontal, vertical


def parse_input_2(data):
    horizontal = 0
    vertical = 0
    aim = 0
    for line in data:
        command, count = line.split()
        if command == 'forward':
            horizontal += int(count)
            vertical += aim * int(count)
        if command == 'up':
            aim -= int(count)
        if command == 'down':
            aim += int(count)
    return horizontal, vertical


if __name__ == '__main__':
    from aocd.models import Puzzle
    puzzle = Puzzle(year=2021, day=2)
    data = puzzle.input_data.splitlines()

    h, v = parse_input(data)
    print(h*v)

    h, v = parse_input_2(data)
    print(h*v)
