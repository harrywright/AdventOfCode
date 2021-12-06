import numpy as np


def gamma(data):
    size = len(data[0])
    result = []
    for i in range(size):
        zero = 0
        one = 0
        for line in data:
            if line[i] == '0':
                zero += 1
            else:
                one += 1
        if zero>one:
            result.append('0')
        else:
            result.append('1')
    return int(''.join(result), base=2)


def epsilon(data):
    size = len(data[0])
    result = []
    for i in range(size):
        zero = 0
        one = 0
        for line in data:
            if line[i] == '0':
                zero += 1
            else:
                one += 1
        if zero<one:
            result.append('0')
        else:
            result.append('1')
    return int(''.join(result), base=2)


def o2_generator(data) -> int:
    size = len(data[0])
    bit = 0

    zero = 0
    one = 0
    for line in data:
        if line[bit] == '0':
            zero += 1
        else:
            one += 1



def co2_scrubber(data) -> int:
    pass


if __name__ == '__main__':
    from aocd.models import Puzzle
    puzzle = Puzzle(year=2021, day=3)
    data = puzzle.input_data.splitlines()

    a = np.array([list(line) for line in data], int)
    print(a)

    print(gamma(a), epsilon(data), gamma(data) * epsilon(data))
