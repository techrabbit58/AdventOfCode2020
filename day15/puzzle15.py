"""
Advent Of Code 2020, Day 15.
https://adventofcode.com/2020/day/15
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
    The solution is reasonable fast for low stops, but takes long for
    high stops. I optimized my working solution (which took ages),
    following somme hints and suggestions of Bradley Sward.
    Bradley Sward is currently an Associate Professor at the
    College of DuPage in suburban Chicago, Illinois.
    The final solution takes more than 25 seconds on my
    Raspberry Pi 400.
    """
    spoken = {}
    offset = 1
    for number in puzzle:
        spoken[number] = offset
        offset += 1
    this = 0
    for turn in range(len(puzzle) + 1, stop):
        if this in spoken:
            offset = turn - spoken[this]
            spoken[this] = turn
            this = offset
        else:
            spoken[this] = turn
            this = 0
        if turn % 100000 == 99999:
            print(f'{turn/stop:4.2f}\r', end='')
    return this



if __name__ == '__main__':
    input_records = prepare()

    start = time.perf_counter()
    print('part 1:', solution(input_records), 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', solution(input_records, stop=30000000), 'time', round(time.perf_counter() - start, 4))
