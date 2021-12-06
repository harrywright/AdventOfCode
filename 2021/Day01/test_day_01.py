import day_01


test_input = """
199
200
208
210
200
207
240
269
260
263"""


def test_depth_count():
    assert day_01.depth_count(test_input) == 7


def test_slide_depth_count():
    assert False
