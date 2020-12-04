if __name__ == '__main__':
    data = []
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            data.append(line)

    print(data)
