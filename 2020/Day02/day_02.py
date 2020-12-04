def parse_data(policy: str) -> tuple:
    policy, password = policy.split(': ')
    policy, letter = policy.split(' ')
    min_count, max_count = policy.split('-')
    return int(min_count), int(max_count), letter, password


def check_data_old(data):
    letter = data[2]
    password = data[3]
    min_count = data[0]
    max_count = data[1]
    count = password.count(letter)
    return min_count <= count <= max_count


def check_data_new(data):
    letter = data[2]
    password = data[3]
    pos_1 = data[0]
    pos_2 = data[1]
    if password[pos_1-1:pos_1] == letter and password[pos_2-1:pos_2] != letter: return True
    if password[pos_2-1:pos_2] == letter and password[pos_1-1:pos_1] != letter: return True
    return False


data = []

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        data.append(parse_data(line))

total = 0
for entry in data:
    if check_data_new(entry): total = total + 1
print(total)