"""
Advent Of Code 2020.
Day 5.
"""
import time

input_file = 'input05.txt'


def parse(fn):
    with open(fn) as fh:
        puzzle = fh.read().strip().split('\n')
    return puzzle


TRANSLATION = str.maketrans('BFRL', '1010')


def translate(seat_code):
    return int(seat_code.translate(TRANSLATION), 2)


def part1(seats_):
    return seats_[-1]


def part2(seats_):
    missing = None
    for x in range(1, len(seats_)):
        missing = seats_[x] - 1
        if seats_[x - 1] < missing < seats_[x]:
            break
        x += 1
    return missing


def part2b(seats_):
    """
    Optimized: Calculate missing seat without using an
    explicit loop. Thanks to Mr Gauss, and thanks to
    Mr. Jens Gutow, who left his clever solution
    as a comment under the Day 5 video of Vlogger
    "Gravitar" on YouTube. O(1) is obviously better
    than O(n).
    """
    return (seats_[-1] + seats_[0]) * (len(seats_) + 1) // 2 - sum(seats_)


if __name__ == '__main__':
    puzzle_input = parse(input_file)
    seats = sorted(translate(seat_code) for seat_code in puzzle_input)

    start = time.perf_counter()
    print('part 1:', part1(seats), 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(seats), 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2b:', part2b(seats), 'time', round(time.perf_counter() - start, 4))
