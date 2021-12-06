import numpy as np


def parse_input(data: list[str]) -> np.array:
    return np.array([list(line) for line in data], int)


def gamma(data: np.array) -> int:
    rows, cols = data.shape
    sums = data.sum(axis=0)

    most_common_bits = ['1' if element >= (rows/2) else '0' for element in sums]
    return int(''.join(most_common_bits), base=2)


def epsilon(data: np.array) -> int:
    rows, cols = data.shape
    sums = data.sum(axis=0)

    least_common_bits = ['1' if element < (rows/2) else '0' for element in sums]
    return int(''.join(least_common_bits), base=2)


def o2_generator(data: np.array) -> int:
    for i in range(data.shape[1]):
        most_common_bits = [1 if element >= (data.shape[0]/2) else 0 for element in data.sum(axis=0)]
        data_filter = [True if row[i] == most_common_bits[i] else False for row in data]
        data = data[data_filter]
        if data.shape[0] == 1:
            break
    return int(''.join(str(i) for i in data[0]), base=2)


def co2_scrubber(data) -> int:
    for i in range(data.shape[1]):
        least_common_bits = [1 if element < (data.shape[0]/2) else 0 for element in data.sum(axis=0)]
        data_filter = [True if row[i] == least_common_bits[i] else False for row in data]
        data = data[data_filter]
        if data.shape[0] == 1:
            break
    return int(''.join(str(i) for i in data[0]), base=2)


if __name__ == '__main__':
    from aocd.models import Puzzle
    puzzle = Puzzle(year=2021, day=3)

    report = parse_input(puzzle.input_data.splitlines())

    print(f'Power consumption: {gamma(report) * epsilon(report)}')
    print(f'Life support rating: {o2_generator(report) * co2_scrubber(report)}')
