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
    puzzle = Puzzle(year=2022, day=1)
    puzzle_input = puzzle.input_data.splitlines()

    parsed_input = []
    temp = []
    for line in puzzle_input:
        if line == '':
            parsed_input.append(temp)
            temp = []
            continue
        temp.append(int(line))

    print(max(sum(elf) for elf in parsed_input))

    sums = [sum(elf) for elf in parsed_input]
    sums.sort(reverse=True)
    print(sums[0]+sums[1]+sums[2])

