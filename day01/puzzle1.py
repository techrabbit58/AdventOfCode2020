"""
Day 01.
Puzzle 1.
Find, from a set of numbers, the two numbers that, when added,
give 2020 as a result.
Return the product of these two numbers.
"""

puzzle_input = 'day01.txt'


def solution(puzzle_input: str):
    with open(puzzle_input) as f:
        numbers = {int(x) for x in f.read().strip().split()}
    for p in sorted(numbers):
        q = 2020 - p
        if q in numbers:
            result = p * q
            break
    return result


if __name__ == '__main__':
    print(solution(puzzle_input))
