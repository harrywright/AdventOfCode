def count_trees(data, spec):
    right = spec[0]
    down = spec[1]
    height = len(data)
    width = len(data[0])

    trees = 0

    x = 0
    for y in range(0, height, down):
        if data[y][x] == '#':
            trees += 1
        x = (x + right) % width

    return trees


if __name__ == '__main__':
    data = []
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            data.append(line)

    print(count_trees(data, (1,1)))
    print(count_trees(data, (3,1)))
    print(count_trees(data, (5,1)))
    print(count_trees(data, (7,1)))
    print(count_trees(data, (1,2)))