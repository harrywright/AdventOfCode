from .day_03 import *

data = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010']


def test_gamma():
    assert gamma(parse_input(data)) == 22


def test_epsilon():
    assert epsilon(parse_input(data)) == 9


def test_o2_generator():
    assert o2_generator(parse_input(data)) == 23


def test_co2_scrubber():
    assert co2_scrubber(parse_input(data)) == 10
