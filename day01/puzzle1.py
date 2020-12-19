"""
Advent Of Code 2020. Day 01. Puzzle 1.
Find, from a set of numbers, the two numbers that, when added,
give 2020 as a result.
Return the production of these two numbers.
"""
input_file = 'day01.txt'


def solution(puzzle_input):
    with open(puzzle_input) as f:
        numbers = {int(x) for x in f.read().strip().split()}
    result = None
    for p in sorted(numbers):
        q = 2020 - p
        if q in numbers:
            result = p * q
            break
    return result


if __name__ == '__main__':
    print(solution(input_file))
