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
            rules[int(head)].append(token.group(1))
            terminals.append([token.group(1)])
            continue
        if '|' in tail:
            sublists = tail.split('|')
            for s in sublists:
                parts = [int(n) for n in list(re.findall(r'(\d+)', s))]
                rules[int(head)].append(parts)
        else:
            parts = [int(n) for n in list(re.findall(r'(\d+)', tail))]
            rules[int(head)].append(parts)
    return [t for _, t in sorted(rules.items())], terminals


def check(terminals, rules, message):
    q = deque([(message, [0])])
    while q:
        msg, rule_heads = q.popleft()
        if not msg and not rule_heads:
            # we are done
            return 1
        if not msg or not rule_heads:
            # the message is exhausted, or there is no rule to apply
            continue
        # otherwise we need to apply more rules to the remaining message
        head, *rule_heads = rule_heads
        ex = rules[head]
        if ex in terminals and ex == msg[:1]:
            q.append((msg[1:], rule_heads))
        elif ex in terminals:
            continue
        else:
            for tail in ex:
                q.append((msg, tail + rule_heads))
    return 0


def solution(rules, terminals, messages):
    result = 0
    for m in messages:
        result += check(terminals, rules, list(m))
    return result


if __name__ == '__main__':
    puzzle_input = load(input_file)
    raw_rules, *raw_messages = split_chunks(puzzle_input)

    prepared_rules, prepared_terminals = decode_rules(raw_rules)

    if raw_messages:
        prepared_messages = [message for message in raw_messages[0].split('\n')]
    else:
        prepared_messages = raw_messages

    start = time.perf_counter()
    print('part 1:', solution(prepared_rules, prepared_terminals, prepared_messages),
          'time', round(time.perf_counter() - start, 4))

    prepared_rules[8].append([42, 8])
    prepared_rules[11].append([42, 11, 31])

    start = time.perf_counter()
    print('part 2:', solution(prepared_rules, prepared_terminals, prepared_messages),
          'time', round(time.perf_counter() - start, 4))
