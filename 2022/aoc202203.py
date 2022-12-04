from string import ascii_letters

from aocd import submit
from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input.split("\n")


def part1(data):
    """Solve part 1"""

    # partition the rucksacks evenly
    rucksacks = [(x[:len(x)//2], x[len(x)//2:]) for x in data]

    priorities = 0
    for rucksack in rucksacks:
        
        # find the erroneously packed item
        item = set(rucksack[0]).intersection(set(rucksack[1])).pop()
        # find its priority
        priorities += ascii_letters.index(item) + 1

    return priorities


def part2(data):
    """Solve part 2"""

    groups = [data[i:i+3] for i in range(0,len(data), 3)]
    
    priorities = 0 
    for group in groups:

        # find common item(s) in rucksack 1 and 2
        common = set(group[0]).intersection(group[1])
        # find common item in all rucksacks
        item = common.intersection(group[2]).pop()
        # find its priority
        priorities += ascii_letters.index(item) + 1

    print(priorities)

    return priorities


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    # Connect to the API
    puzzle_input = Puzzle(year=2022, day=3).input_data
    # Solve
    answer1, answer2 = solve(puzzle_input)
    # Submit answers
    submit(answer1, part='a', day=3, year=2022)
    submit(answer2, part='b', day=3, year=2022)
