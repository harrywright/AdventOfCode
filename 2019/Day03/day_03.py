from typing import List, Tuple


def get_points_on_path(path: List[str]) -> List[Tuple[int, int]]:
    points = [(0, 0)]  # type: List[Tuple[int, int]]

    for instruction in path:
        current_point = points[-1]

        direction = instruction[0]
        distance = int(instruction[1:])

        for i in range(distance):
            if direction == 'R':
                points.append((current_point[0] + i + 1, current_point[1]))
            elif direction == 'L':
                points.append((current_point[0] - i - 1, current_point[1]))
            elif direction == 'U':
                points.append((current_point[0], current_point[1] + i + 1))
            elif direction == 'D':
                points.append((current_point[0], current_point[1] - i - 1))

    points.pop(0)
    return points


def get_intersections(path1: List[str], path2: List[str]) -> List[Tuple[int, int]]:
    points1 = get_points_on_path(path1)
    points2 = get_points_on_path(path2)

    return list(set(points1) & set(points2))


def get_closest_point(points: List[Tuple[int, int]]) -> Tuple[int, int]:
    closest_point = None
    for point in points:
        if not closest_point:
            closest_point = point
        elif closest_point and (abs(point[0]) + abs(point[1])) < (abs(closest_point[0]) + abs(closest_point[1])):
            closest_point = point
    return closest_point


def get_closest_intersection(path1: List[str], path2: List[str]) -> Tuple[int, int]:
    intersections = get_intersections(path1, path2)
    return get_closest_point(intersections)


with open('input.txt', 'r') as f:
    input_path1 = f.readline().split(',')
    input_path2 = f.readline().split(',')


print(f'Part 1: Closest {get_closest_intersection(input_path1, input_path2)}')
