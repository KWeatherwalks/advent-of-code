# aoc_template.py
# Modified from https://realpython.com/python-advent-of-code/#a-starting-template

import re
from functools import reduce
from string import ascii_letters

from aocd import submit
from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input.split("\n")


def is_possible(counts):
    too_many_red = counts.get("red", 0) > 12
    too_many_green = counts.get("green", 0) > 13
    too_many_blue = counts.get("blue", 0) > 14
    if too_many_red or too_many_green or too_many_blue:
        return False

    return True


def part1(data):
    """Solve part 1"""
    total = 0
    for game in data:
        # get game id
        game_id, sets = game.split(":")
        game_id = int(game_id.strip(ascii_letters + " "))
        # split into sets
        sets = sets.split(";")
        for set in sets:
            # split into colors
            colors = set.split(", ")
            # convert to dictionary
            counts = {balls.split()[1]: int(balls.split()[0]) for balls in colors}
            if not is_possible(counts):
                game_id = 0
                break
        total += game_id

    return total


def part2(data):
    """Solve part 2"""
    total = 0
    for game in data:
        # get game id
        game_id, sets = game.split(":")
        game_id = int(game_id.strip(ascii_letters + " "))
        # split into sets
        sets = sets.split(";")
        minimals = {"red": 0, "blue": 0, "green": 0}
        for set in sets:
            # split into colors
            colors = set.split(", ")
            # convert to dictionary
            counts = {balls.split()[1]: int(balls.split()[0]) for balls in colors}
            for color, count in counts.items():
                minimals[color] = max(minimals[color], count)
        power = reduce((lambda x, y: x * y), minimals.values())
        total += power
    return total


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    # Connect to the API
    puzzle_input = Puzzle(year=2023, day=2).input_data
    # Solve
    answer1, answer2 = solve(puzzle_input)
    # Submit answers
    submit(answer1, part="a", day=2, year=2023)
    submit(answer2, part="b", day=2, year=2023)
