import re


def contains_double_digit(password: int) -> bool:
    regexp = re.compile(r'(.)\1')
    return bool(re.search(regexp, str(password)))


def contains_only_double_digit(password: int) -> bool:
    """Contains a double that is not part of a longer sequence"""
    word = str(password)

    if word[0] == word[1] and word[0] != word[2]:
        return True
    if word[-2] == word[-1] and word[-2] != word[-3]:
        return True

    for i in range(1, len(word)-2):
        if word[i] == word[i+1] and word[i] != word[i+2] and word[i] != word[i-1]:
            return True

    return False


def never_decreases(password: int) -> bool:
    word = str(password)
    if len(word) == 1:
        return True
    if never_decreases(int(word[1:])) and int(word[0]) <= int(word[1]):
        return True
    return False


count = 0
for i in range(372037, 905158):
    if contains_double_digit(i) and never_decreases(i) and contains_only_double_digit(i):
        count += 1
print(f'Number of possible passwords: {count}')
