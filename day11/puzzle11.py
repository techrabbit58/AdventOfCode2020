"""
Advent Of Code 2020, Day 11.
https://adventofcode.com/2020/day/11
"""
import time

input_file = 'input11.txt'


def load(fn):
    with open(fn) as fh:
        puzzle = fh.read().strip().split('\n')
    return puzzle


def immediate_neighbourhood(location, seats):
    assert seats is not None
    row, col = location
    yield row - 1, col - 1
    yield row - 1, col
    yield row - 1, col + 1
    yield row, col - 1
    yield row, col + 1
    yield row + 1, col - 1
    yield row + 1, col
    yield row + 1, col + 1


def complex_neighbourhood(location, seats):
    row, col = location
    rows, cols  = max(seats, key=lambda s: s[0])[0] + 1, max(seats, key= lambda s: s[1])[1] + 1
    # same row, to the east
    for c in range(col + 1, cols):
        if (row, c) in seats:
            yield (row, c)
            break
    # same row, to the west
    for c in range(col - 1, -1, -1):
        if (row, c) in seats:
            yield (row, c)
            break
    # same column, to the north
    for r in range(row - 1, -1, -1):
        if (r, col) in seats:
            yield (r, col)
            break
    # same column, to the south
    for r in range(row + 1, rows):
        if (r, col) in seats:
            yield (r, col)
            break
    # south western
    for rc in zip(range(row + 1, rows), range(col - 1, -1, -1)):
        if rc in seats:
            yield rc
            break
    # south eastern
    for rc in zip(range(row + 1, rows), range(col + 1, cols)):
        if rc in seats:
            yield rc
            break
    # north eastern
    for rc in zip(range(row - 1, -1, -1), range(col + 1, cols)):
        if rc in seats:
            yield rc
            break
    # north western
    for rc in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if rc in seats:
            yield rc
            break


def locate_seats(puzzle):
    return {(row, col): set()
        for row, line in enumerate(puzzle)
        for col, position in enumerate(line)
        if position != '.'}


def assign_neighbourhood(seats, neighbourhood):
    for seat, neighbours in seats.items():
        for candidate in neighbourhood(seat, seats):
            if candidate in seats:
                neighbours.add(candidate)


def occupy(seat, neighbours, occupied, *, threshold):
    num_neighbours = len(neighbours.intersection(occupied))
    if num_neighbours == 0:
        return True
    if num_neighbours >= threshold:
        return False
    return seat in occupied


def part1(seats):
    occupied, last_occupied = {}, None
    while occupied != last_occupied:
        last_occupied = occupied
        occupied = {seat for seat in seats if occupy(seat, seats[seat], occupied, threshold=4)}
    return len(occupied)


def part2(seats):
    occupied, last_occupied = {}, None
    while occupied != last_occupied:
        last_occupied = occupied
        occupied = {seat for seat in seats if occupy(seat, seats[seat], occupied, threshold=5)}
    return len(occupied)


if __name__ == '__main__':
    puzzle_input = load(input_file)
    seat_locations = locate_seats(puzzle_input)

    start = time.perf_counter()
    assign_neighbourhood(seat_locations, immediate_neighbourhood)
    print('part 1:', part1(seat_locations), 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    assign_neighbourhood(seat_locations, complex_neighbourhood)
    print('part 2:', part2(seat_locations), 'time', round(time.perf_counter() - start, 4))
