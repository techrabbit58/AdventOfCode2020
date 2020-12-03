"""
Prepare directory and files for a new day of Advent Of Code 2020.
"""
import os

if __name__ == '__main__':

    day = int(input('Day? '))
    if not 1 <= day <= 24:
        print('Day must be a number from 1 to 24.')
        print('Please, try again.')
        exit()
    
    folder = f'day{day:02d}'
    if os.path.exists(folder):
        print(f'Folder "{folder}" already there.')
    else:
        os.mkdir(folder)
    
    os.chdir(folder)
    
    input_file = f'input{day:02d}.txt'
    if os.path.exists(input_file):
        print(f'Puzzle input file "{input_file}" already there.')
    else:
        with open(input_file, 'w'):
            pass

    puzzles = [f'puzzle{day:02d}-1.py', f'puzzle{day:02d}-2.py']

    for n, puzzle in enumerate(puzzles, 1):

        template = [
                '"""',
                f'Advent Of Code 2020. Day {day}. Puzzle {n}.',
                '"""',
                'import time',
                '',
                f"input_file = '{input_file}'",
                '',
                '',
                'def parse(puzzle_input):',
                '    with open(puzzle_input) as f:',
                "        puzzle = f.read().strip().split('\\n')",
                '    return puzzle',
                '',
                '',
                'def solution(puzzle):',
                '    result = puzzle',
                '    return result',
                '',
                '',
                "if __name__ == '__main__':",
                '    puzzle = parse(input_file)',
                '    start = time.perf_counter()',
                '    print(solution(puzzle), time.perf_counter() - start)',
                ]

        if os.path.exists(puzzle):
            print(f'Python solution "{puzzle}" already there.')
        else:
            with open(puzzle, 'w') as f:
                for line in template:
                    print(line, file=f)
