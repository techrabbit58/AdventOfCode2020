"""
Advent Of Code 2020, Day 19.
https://adventofcode.com/2020/day/19
"""
import re
import time
from collections import defaultdict, deque

# input_file = "test19c.txt"
input_file = 'input19.txt'


def load(fn):
    with open(fn) as fh:
        return fh.read().strip()


def split_chunks(raw_input):
    return raw_input.split('\n\n')


def decode_rules(text):
    terminals = []
    rules = defaultdict(list)
    for line in text.strip().split('\n'):
        head, tail = line.split(':')
        if tail.strip().startswith('"'):
            token = re.search(r'"([ab])"', tail)
            rules[head].append(token.group(1))
            terminals.append([token.group(1)])
            continue
        if '|' in tail:
            sublists = tail.split('|')
            for s in sublists:
                parts = list(re.findall(r'(\d+)', s))
                rules[head].append(parts)
        else:
            parts = list(re.findall(r'(\d+)', tail))
            rules[head].append(parts)
    return rules, terminals


def expand(product, rules, terminals, words):
    product = [rules[s][0] if rules[s] in terminals else s for s in product]
    for i, s in enumerate(product):
        if s in terminals:
            continue
        for ex in rules[s]:
            yield product[:i] + ex + product[i + 1:]
    if len(product) == len([s for s in product if [s] in terminals]):
        words.add(''.join(product))
    yield product


def recognize(terminals, rules, product, message, words):
    print(words)
    if ''.join(product) in words:
        return 1
    all_products = set()
    q = deque()
    q.append(product)
    all_products.add('.'.join(product))
    while q:
        p = q.popleft()
        if p == message:
            return 1
        for next_p in expand(p, rules, terminals, words):
            s = '.'.join(next_p)
            if s not in all_products:
                q.append(next_p)
                all_products.add(s)
    return 0


def part1(rules, terminals, messages):
    known_words = set()
    return sum(recognize(terminals, rules, ['0'], list(m), known_words) for m in messages)


def part2(rules, terminals, messages):
    return len(rules), len(terminals), len(messages)


if __name__ == '__main__':
    puzzle_input = load(input_file)
    raw_rules, *raw_messages = split_chunks(puzzle_input)

    prepared_rules, prepared_terminals = decode_rules(raw_rules)

    if raw_messages:
        prepared_messages = [message for message in raw_messages[0].split('\n')]
    else:
        prepared_messages = raw_messages

    start = time.perf_counter()
    print('part 1:', part1(prepared_rules, prepared_terminals, prepared_messages),
          'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(prepared_rules, prepared_terminals, prepared_messages),
          'time', round(time.perf_counter() - start, 4))
