"""
Advent Of Code 2020, Day 12.
https://adventofcode.com/2020/day/12
"""
import time

input_file = 'input12.txt'


def load(fn):
    with open(fn) as fh:
        puzzle = [(ins[0], int(ins[1:])) for ins in fh.read().strip().split('\n')]
    return puzzle


def navigate(position, heading, action, value):
    east, north = position
    d_east, d_north = heading
    if action == 'N':
        north += value
    elif action == 'S':
        north -= value
    elif action == 'E':
        east += value
    elif action == 'W':
        east -= value
    elif action == 'F':
        east, north = east + value * d_east, north + value * d_north
    elif action == 'L':
        d_east, d_north = {90: (-d_north, d_east), 180: (-d_east, -d_north), 270: (d_north, -d_east)}[value]
    elif action == 'R':
        d_east, d_north = {270: (-d_north, d_east), 180: (-d_east, -d_north), 90: (d_north, -d_east)}[value]
    else:
        raise ValueError(f'bad action "{action}"')
    return (east, north), (d_east, d_north)


def part1(puzzle):
    ship = 0, 0
    heading = 1, 0
    for action, value in puzzle:
        ship, heading = navigate(ship, heading, action, value)
    east, north = ship
    return abs(east) + abs(north)


def part2(puzzle):
    ship = 0, 0
    waypoint = 10, 1
    for action, value in puzzle:
        if action == 'F':
            ship, _ = navigate(ship, waypoint, action, value)
        elif action in 'NEWS':
            waypoint, _ = navigate(waypoint, waypoint, action, value)
        else:
            _, waypoint = navigate(waypoint, waypoint, action, value)
    east, north = ship
    return abs(east) + abs(north)


if __name__ == '__main__':
    puzzle_input = load(input_file)

    start = time.perf_counter()
    print('part 1:', part1(puzzle_input), 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(puzzle_input), 'time', round(time.perf_counter() - start, 4))
