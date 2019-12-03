from day_03 import get_closest_intersection, get_quickest_intersection, steps_to_point

test1 = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
test2 = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
test3 = ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51']
test4 = ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']


def test_get_closest_intersection():
    closest = get_closest_intersection(test1, test2)
    assert closest[0] + closest[1] == 159
    closest = get_closest_intersection(test3, test4)
    assert closest[0] + closest[1] == 135


def test_get_quickest_intersection():
    quickest = get_quickest_intersection(test1, test2)
    assert steps_to_point(test1, quickest) + steps_to_point(test2, quickest) == 610
    quickest = get_quickest_intersection(test3, test4)
    assert steps_to_point(test3, quickest) + steps_to_point(test4, quickest) == 410
