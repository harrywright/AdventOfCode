import functools
import itertools
import operator

from typing import List


def find_entries_with_sum(data: List[int], target: int, count: int) -> None:
    for entries in itertools.combinations(data, count):
        if sum(entries) == target:
            print(f'{entries} => {functools.reduce(operator.mul, entries)}')


if __name__ == '__main__':
    data = []

    with open("input.txt") as f:
        for line in f:
            line.strip()
            data.append(int(line))

    find_entries_with_sum(data, 2020, 2)
    find_entries_with_sum(data, 2020, 3)
