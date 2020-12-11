"""
Advent Of Code 2020, Day 11.
https://adventofcode.com/2020/day/11
"""
import time

input_file = 'test11.txt'


def load(fn):
    with open(fn) as fh:
        puzzle = fh.read().strip().split('\n')
    return puzzle


def locate_seats(puzzle):
    return {
        (row, col) for row, line in enumerate(puzzle)
        for col, position in enumerate(line)
        if position == 'L'}, len(puzzle[0]), len(puzzle)


def immediate_neighbourhood(location):
    row, col = location
    yield row - 1, col - 1
    yield row - 1, col
    yield row - 1, col + 1
    yield row, col - 1
    yield row, col + 1
    yield row + 1, col - 1
    yield row + 1, col
    yield row + 1, col + 1


def simple_occupy(seat, seats, occupied):
    num_neighbours = 0
    for location in immediate_neighbourhood(seat):
        if location in seats:
            num_neighbours += 1 if location in occupied else 0
    if num_neighbours == 0:
        return True
    if num_neighbours >= 4:
        return False
    return seat in occupied


def part1(seats):
    occupied, last_occupied = {}, None
    while occupied != last_occupied:
        last_occupied = occupied
        occupied = {seat for seat in seats if simple_occupy(seat, seats, occupied)}
    return len(occupied)


def part2(seats, rows, columns):
    occupied, last_occupied = {}, None
    return len(occupied), rows, columns


if __name__ == '__main__':
    puzzle_input = load(input_file)
    seat_locations, rows, columns = locate_seats(puzzle_input)

    start = time.perf_counter()
    print('part 1:', part1(seat_locations), 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(seat_locations, rows, columns), 'time', round(time.perf_counter() - start, 4))
