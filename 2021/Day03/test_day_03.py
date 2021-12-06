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
    assert gamma(data) == 22


def test_epsilon():
    assert epsilon(data) == 9

