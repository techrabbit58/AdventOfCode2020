"""
Advent Of Code 2020. Day 02. Puzzle 1.
Given a list of strings, written line by line together with a so called
policy:

    p-q ch: string

where:

    p is the first position in the string, where 1st position counts from 1
    q is the second position in the string, where 2nd position counts from 1
    ch is a character from a set of 'a' to 'z'
    ch may occur only in one of both positions, but not in both.
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
        if (s[p - 1] == ch) != (s[q - 1] == ch):
            result += 1
    return result


if __name__ == '__main__':
    words = parse(input_file)
    start = time.perf_counter()
    print(solution(words), time.perf_counter() - start)
