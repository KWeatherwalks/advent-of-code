from aocd import submit
from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input"""
    elves = puzzle_input.input_data.split("\n\n")
    elves = [elf.split() for elf in elves]
    
    return list(map(lambda x: [int(y) for y in x], elves))

def part1(data):
    return max([sum(elf) for elf in data])

def part2(data):
    top_three = sorted([sum(elf) for elf in data], reverse=True)[:3]
    return sum(top_three)

def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    solutions = solve(Puzzle(year=2022, day=1))
    submit(solutions[0], part='a')
    submit(solutions[1], part='b')