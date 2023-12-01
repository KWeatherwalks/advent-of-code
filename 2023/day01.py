# aoc_template.py
# Modified from https://realpython.com/python-advent-of-code/#a-starting-template

from string import ascii_letters

from aocd import submit
from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input.split("\n")


def part1(data):
    """Solve part 1"""
    values = []
    for line in data:
        digits_only = [
            character for character in line if character not in ascii_letters
        ]
        calibration_value = int(digits_only[0] + digits_only[-1])
        values.append(calibration_value)
    return sum(values)


def replace_words(s):
    output = (
        s.replace("one", "o1ne")
        .replace("two", "t2wo")
        .replace("three", "t3hree")
        .replace("four", "u4r")
        .replace("five", "i5v")
        .replace("six", "i6x")
        .replace("seven", "v7n")
        .replace("eight", "i8ht")
        .replace("nine", "i9ne")
    )
    return output


def part2(data):
    """Solve part 2"""
    values = []
    for line in data:
        words_converted = replace_words(line)
        digits_only = [
            character for character in words_converted if character not in ascii_letters
        ]
        calibration_value = int(digits_only[0] + digits_only[-1])
        values.append(calibration_value)

    return sum(values)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    # Connect to the API
    puzzle_input = Puzzle(year=2023, day=1).input_data
    # Solve
    answer1, answer2 = solve(puzzle_input)
    # Submit answers
    submit(answer1, part="a", day=1, year=2023)
    submit(answer2, part="b", day=1, year=2023)
