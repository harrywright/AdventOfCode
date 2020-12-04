import itertools

data = []

with open("input.txt") as f:
    for line in f:
        line.strip()
        data.append(int(line))

for n1 in data:
    for n2 in data:
        if n1 + n2 == 2020:
            print(f'{n1} {n2} {n1 + n2} {n1 * n2}')

for n1 in data:
    for n2 in data:
        for n3 in data:
            if n1 + n2 + n3 == 2020:
                print(f'{n1} {n2} {n3} {n1 + n2 + n3} {n1 * n2 * n3}')


for entries in itertools.combinations(data, 2):
    if sum(entries) == 2020:
        print(f'{entries}')

for entries in itertools.combinations(data, 3):
    if sum(entries) == 2020:
        print(f'{entries}')
