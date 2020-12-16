"""
Advent Of Code 2020, Day 16.
https://adventofcode.com/2020/day/16
"""
import time
import re

# input_file = 'test16a.txt'
input_file = 'test16b.txt'
# input_file = 'input16.txt'


def load(fn):
    with open(fn) as fh:
        return fh.read().strip()


def prepare(raw_input):
    """
    Input is organized in three chunks: (1) rules, (2) my ticket, (3) tickets nearby.
    Must be prepared following different rules.
        (1) label ':' lower 'or' upper ',' lower 'or' upper
        (2) header line "your ticket:" followed by one line of comma separated integers
        (3) same as (2), but many lines of comma separated integers
    The CSV lines have always as many fields as there are rules in (1).
    """
    rules, my_ticket, tickets_nearby = [line for line in raw_input.split('\n\n')]
    return rules, my_ticket, tickets_nearby


rule_split = re.compile(r'([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)')


def parse_rules(raw):
    rules = {}
    for group in rule_split.findall(raw):
        label, a, b, c, d = group
        rules[label] = {i for i in range(int(a), int(b) + 1)} | {i for i in range(int(c), int(d) + 1)}
    return rules


def parse_tickets(raw):
    tickets = []
    for line in raw.split('\n'):
        if line in {'your ticket:', 'nearby tickets:'}:
            continue
        tickets.append([int(i) for i in line.split(',')])
    return tickets


def part1(rules, tickets):
    valid_values = set()
    good_tickets = []
    for values in rules.values():
        valid_values.update(values)
    errors = 0
    for ticket in tickets:
        errors_so_far = errors
        for field in ticket:
            if field not in valid_values:
                errors += field
        if errors - errors_so_far == 0:
            good_tickets.append(ticket)
    return good_tickets, errors


def transpose(matrix):
    result = [[] for _ in range(len(matrix[0]))]
    for y, row in enumerate(matrix):
        for x, col in enumerate(row):
            result[x].append(matrix[y][x])
    return result


def part2(rules, mine, others):
    """NOT SOLVED!"""
    tickets = others.copy() + [mine]
    fields = transpose(tickets)
    num_fields = len(rules)
    candidates = {n: set() for n in range(num_fields)}
    for n, field in enumerate(fields):
        for label, rule in rules.items():
            if rule.intersection(field):
                candidates[n].add(label)
    return candidates


if __name__ == '__main__':
    puzzle_input = load(input_file)
    raw_rules, raw_my_ticket, raw_tickets_nearby = prepare(puzzle_input)
    rule_base = parse_rules(raw_rules)
    my_ticket = parse_tickets(raw_my_ticket)[0]
    nearby_tickets = parse_tickets(raw_tickets_nearby)

    start = time.perf_counter()
    valid_tickets, error_rate = part1(rule_base, nearby_tickets)
    print('part 1:', error_rate, 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(rule_base, my_ticket, valid_tickets), 'time', round(time.perf_counter() - start, 4))
