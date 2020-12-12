"""
Advent Of Code 2020, Day 12.
https://adventofcode.com/2020/day/12
Instead of 2D vectors, complex numbers can be used, which all in all is faster
and gives shorter code. This alternate solution is a tribute to GitHub user "fuglede":
https://github.com/fuglede/adventofcode/tree/master/2020
"""
import time

input_file = '../day12/input12.txt'


def load(fn):
    with open(fn) as fh:
        puzzle = [(ins[0], int(ins[1:])) for ins in fh.read().strip().split('\n')]
    return puzzle


direction = {'N': 1j, 'E': 1, 'W': -1, 'S': -1j}
rotation = {'L': 1j, 'R': -1j}


def part1(puzzle):
    ship = 0
    heading = 1
    for action, value in puzzle:
        if action in direction:
            ship += direction[action] * value
        elif action in rotation:
            heading *= rotation[action] ** (value / 90)
        else:
            ship += value * heading
    return int(abs(ship.real) + abs(ship.imag))


def part2(puzzle):
    ship = 0
    waypoint = 10 + 1j
    for action, value in puzzle:
        if action in direction:
            waypoint += direction[action] * value
        elif action in rotation:
            waypoint *= rotation[action] ** (value / 90)
        else:
            ship += value * waypoint
    return int(abs(ship.real) + abs(ship.imag))


if __name__ == '__main__':
    puzzle_input = load(input_file)

    start = time.perf_counter()
    print('part 1:', part1(puzzle_input), 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(puzzle_input), 'time', round(time.perf_counter() - start, 4))
