"""
Advent Of Code 2020, Day 15.
https://adventofcode.com/2020/day/15
This puzzle has some relation to the so called "Van Eck Sequence".
"""
import time


def prepare():
    """
    Given 0,3,6, the 2020th number spoken is 436.
    Given 0,3,6, the 30000000th number spoken is 175594.
    """
    return [1, 0, 15, 2, 10, 13]
    # return [0, 3, 6]


def solution(puzzle, stop=2020):
    """
    The solution is reasonably fast for low stops, but takes long for
    high stops. I optimized my already working solution (which unfortunately
    took ages of runtime for part 2), following somme hints and suggestions of
    Bradley Sward. Bradley Sward is currently an Associate Professor at the
    College of DuPage in suburban Chicago, Illinois. The final result takes
    about 30 seconds on a Raspberry Pi 400, for part 2.
    """
    spoken = {number: offset for offset, number in enumerate(puzzle, 1)}
    this = 0
    for turn in range(len(puzzle) + 1, stop):
        if this in spoken:
            spoken[this], this = turn, turn - spoken[this]
        else:
            spoken[this], this = turn, 0
        if turn % 100000 == 99999:
            print(f'{turn / stop:4.2f}')
    return this


def solution_b(puzzle, stop=2020):
    """
    This next solution is even faster, about 25%, thanks to Gravitar64.
    https://github.com/Gravitar64/Advent-of-Code-2020
    Counting the turns from len(puzzle) instead of len(puzzle) + 1 makes
    everything so easy and nice!
    """
    spoken = {last: turn for turn, last in enumerate(puzzle, 1)}
    last = puzzle[-1]
    for turn in range(len(puzzle), stop):
        recent = spoken.get(last, turn)
        spoken[last] = turn
        last = turn - recent
    return last


def recitation(puzzle):
    from itertools import count

    def iterate():
        spoken = {last: turn for turn, last in enumerate(puzzle, 1)}
        last = puzzle[-1]
        for turn in count(len(puzzle)):
            recent = spoken.get(last, turn)
            spoken[last] = turn
            last = turn - recent
            yield turn + 1, last

    return iterate


def solution_c(puzzle, stop=2020):
    """
    The "lazy" approach is relatively slow. Didn't expect that.
    Possibly because of the explicit stop condition in the main loop?
    """
    memory_game = recitation(puzzle)
    for turn, last in memory_game():
        if turn == stop:
            return last


if __name__ == '__main__':
    input_records = prepare()

    start = time.perf_counter()
    print('part 1:', solution_b(input_records), 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', solution_b(input_records, stop=30000000), 'time', round(time.perf_counter() - start, 4))
