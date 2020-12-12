"""
Advent Of Code 2020, Day 12.
https://adventofcode.com/2020/day/12
"""
import time

input_file = 'input12.txt'


def load(fn):
    with open(fn) as fh:
        puzzle = fh.read().strip().split('\n')
    return puzzle


def navigate(position, heading, instruction):
    action, value = instruction[0].upper(), int(instruction[1:])
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
        east += value * d_east
        north += value * d_north
    elif instruction in {'L90', 'R270'}:
        d_east, d_north = -d_north, d_east
    elif instruction in {'L180', 'R180'}:
        d_east, d_north = -d_east, -d_north
    elif instruction in {'L270', 'R90'}:
        d_east, d_north = d_north, -d_east
    else:
        raise ValueError(f'nad action "{action}"')
    return (east, north), (d_east, d_north)


def part1(puzzle):
    ship = 0, 0
    heading = 1, 0
    for instruction in puzzle:
        ship, heading = navigate(ship, heading, instruction)
    east, north = ship
    return abs(east) + abs(north)


def part2(puzzle):
    ship = (0, 0)
    waypoint = (10, 1)
    print(ship, waypoint)
    for instruction in puzzle:
        if instruction.startswith('F'):
            ship, _ = navigate(ship, waypoint, instruction)
        elif instruction[0] in 'NEWS':
            waypoint, _ = navigate(waypoint, waypoint, instruction)
        else:
            _, waypoint = navigate(waypoint, waypoint, instruction)
        print(ship, waypoint)
    east, north = ship
    return abs(east) + abs(north)


if __name__ == '__main__':
    puzzle_input = load(input_file)

    start = time.perf_counter()
    print('part 1:', part1(puzzle_input), 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(puzzle_input), 'time', round(time.perf_counter() - start, 4))
