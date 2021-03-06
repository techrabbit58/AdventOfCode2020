"""
Advent Of Code 2020. Day 02. Puzzle 1.
Given a list of strings, written line by line together with a so called
policy:

    p-q ch: string

where:

    p is the minimum required count of character ch in string
    q is the allowed maximum count of ch in string
    ch is a character from a set of 'a' to 'z'
    : is simply a colon that separates the policy from the string
    string is the string under test.

Result: number of strings that comply to their line policy.
"""
import time

input_file = 'day02.txt'


def parse(puzzle_input):
    with open(puzzle_input) as f:
        lines = f.read().strip().splitlines()
        words = []
        for line in lines:
            policy, _, s = line.rpartition(':')
            p, _, rest = policy.partition('-')
            q, _, ch = rest.partition(' ')
            words.append((int(p), int(q), ch.strip(), s.strip()))
        return words


def solution(words):
    result = 0
    for p, q, ch, s in words:
        if p <= s.count(ch) <= q:
            result += 1
    return result


if __name__ == '__main__':
    words = parse(input_file)
    start = time.perf_counter()
    print(solution(words), time.perf_counter() - start)
