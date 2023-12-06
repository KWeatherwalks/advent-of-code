# aoc_template.py
# Modified from https://realpython.com/python-advent-of-code/#a-starting-template

import math
from pprint import pprint
from string import digits, printable

from aocd import submit
from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input"""
    pad = "."
    data = [[pad] + list(line) + [pad] for line in puzzle_input.split("\n")]
    n = len(data[0])
    # pad top and bottom
    output = [[pad] * n] + data + [[pad] * n]
    return output


def get_neighbors(i, j):
    """Finds all index pairs around a given coordinate"""
    return [
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j - 1),
        (i, j + 1),
        (i + 1, j - 1),
        (i + 1, j),
        (i + 1, j + 1),
    ]


def is_symbol(c):
    """Checks if character is a symbol"""
    is_printable = c in printable
    is_digit = c in digits
    is_period = c == "."
    return is_printable and not is_digit and not is_period


def part1(data):
    """Solve part 1"""
    total = 0
    # search iteratively through the indices of the matrix
    for row in range(1, len(data) - 1):
        for col in range(1, len(data[0]) - 1):
            #  when a symbol is encountered, search surrounding cells for digits
            if is_symbol(data[row][col]):
                for ni, nj in get_neighbors(row, col):
                    #  if a digit is encountered, search prior digits and following digits
                    if (character := data[ni][nj]) in digits:
                        number_string = character
                        #  alter matrix to remove the digits by replacing each digit with a .
                        data[ni][nj] = "."
                        # get preceding digits in row
                        j = nj - 1
                        while (digit := data[ni][j]) in digits:
                            number_string = digit + number_string
                            data[ni][j] = "."
                            j -= 1

                        # get following digits in row
                        j = nj + 1
                        while (digit := data[ni][j]) in digits:
                            number_string += digit
                            data[ni][j] = "."
                            j += 1

                        #  store number and add to total
                        total += int(number_string)
                    #  repeat

    # return the total
    return total


def get_part_numbers(data: list[list[str]], row_number: int, col_number: int) -> list:
    temp_matrix = data.copy()
    part_numbers = []

    for ni, nj in get_neighbors(row_number, col_number):
        # if a digit is encountered, search prior digits and following digits
        if (character := temp_matrix[ni][nj]) in digits:
            number_string = character

            #  alter matrix to remove the digits by replacing each digit with a .
            temp_matrix[ni][nj] = "."

            # get preceding digits in row
            j = nj - 1
            while (digit := temp_matrix[ni][j]) in digits:
                number_string = digit + number_string
                temp_matrix[ni][j] = "."
                j -= 1

            # get following digits in row
            j = nj + 1
            while (digit := temp_matrix[ni][j]) in digits:
                number_string += digit
                temp_matrix[ni][j] = "."
                j += 1

            part_numbers.append(int(number_string))

    if len(part_numbers) == 2:
        data = temp_matrix.copy()
        return part_numbers


def part2(data):
    """Solve part 2"""
    total = 0
    # search iteratively through the indices of the matrix
    for row in range(1, len(data) - 1):
        for col in range(1, len(data) - 1):
            # if * symbol encountered, search surrounding cells for part numbers
            if data[row][col] == "*":
                # capture list of part numbers
                if parts_list := get_part_numbers(data, row, col):
                    # calculate gear ratio
                    total += math.prod(parts_list)

    return total


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    solution1 = part1(parse(puzzle_input))
    solution2 = part2(parse(puzzle_input))

    return solution1, solution2


if __name__ == "__main__":
    # Connect to the API
    puzzle_input = Puzzle(year=2023, day=3).input_data
    # Solve
    answer1, answer2 = solve(puzzle_input)
    # Submit answers
    submit(answer1, part="a", day=3, year=2023)
    submit(answer2, part="b", day=3, year=2023)


"""Patterns
d..     d..     d..     d..     d..     d.d
d*.     .*.     .*.     .*.     .*d     .*.
...     d..     .d.     ..d     ...     ...

.d.     .d.     .d.     .d.     .d.
d*.     .*.     .*.     .*.     .*d
...     d..     .d.     ..d     ...

..d     ..d     ..d     ..d
d*.     .*.     .*.     .*.
...     d..     .d.     ..d

...     ...     ...
d*d     .*d     .*d
...     d..     .d.

...     ...
d*.     .*.
..d     d.d

...
d*.
.d.
"""
