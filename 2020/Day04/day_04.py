from typing import List, Union


def scan_passport(passport: str) -> bool:
    required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    total = 0
    for required_key in required_keys:
        if required_key in passport:
            total += 1

    if total == 7:
        return True
    else:
        return False


def parse_input(input_data: str) -> Union[List[dict], None]:
    if not input_data:
        return None

    result = []
    passport = {}

    for line in input_data.split("\n"):
        if line == "":
            if passport:
                result.append(passport)
            passport = {}
            continue
        for item in line.split(" "):
            passport[item.split(":")[0]] = item.split(":")[1]

    if passport:
        result.append(passport)
    return result


if __name__ == '__main__':
    with open("input.txt") as f:
        data = f.read()
        passports = parse_input(data)

    valid = 0
    for passport in passports:
        if scan_passport(passport):
            valid += 1

    print(valid)
