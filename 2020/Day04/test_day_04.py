from .day_04 import *

import pytest


def example_input_data():
    return """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""


def example_parsed_data():
    return [
        {"ecl": "gry",
         "pid": "860033327",
         "eyr": "2020",
         "hcl": "#fffffd",
         "byr": "1937",
         "iyr": "2017",
         "cid": "147",
         "hgt": "183cm"
         },

        {"iyr": "2013",
         "ecl": "amb",
         "cid": "350",
         "eyr": "2023",
         "pid": "028048884",
         "hcl": "#cfa07d",
         "byr": "1929"},

        {"hcl": "#ae17e1",
         "iyr": "2013",
         "eyr": "2024",
         "ecl": "brn",
         "pid": "760753108",
         "byr": "1931",
         "hgt": "179cm"},

        {"hcl": "#cfa07d",
         "eyr": "2025",
         "pid": "166559648",
         "iyr": "2011",
         "ecl": "brn",
         "hgt": "59in"}
    ]


@pytest.mark.parametrize("input_data, parsed_data", [
    ("", None),
    ("test:test", [{"test": "test"}]),
    ("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd", [{"ecl": "gry", "pid": "860033327", "hcl": "#fffffd", "eyr": "2020"}]),
    ("abc:abc def:def\nghi:ghi", [{"abc": "abc", "def": "def", "ghi": "ghi"}]),
    ("abc:abc def:def\n\nghi:ghi", [{"abc": "abc", "def": "def"}, {"ghi": "ghi"}]),
    (example_input_data(), example_parsed_data()),
])
def test_parse_input(input_data, parsed_data):
    assert parse_input(input_data) == parsed_data


def test_scan_passport():
    assert False
