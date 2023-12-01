# aoc_template.py
# Modified from https://realpython.com/python-advent-of-code/#a-starting-template

from aocd import submit
from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input


class Sleigh:
    def __init__(self):
        self.houses_visited = {(0, 0): 1}
        self.location = (0, 0)

    def visit_house(self):
        self.houses_visited[self.location] = (
            self.houses_visited.get(self.location, 0) + 1
        )

    def drive_to_next_house(self, direction):
        if direction == ">":
            self.location = (self.location[0] + 1, self.location[1])
        if direction == "v":
            self.location = (self.location[0], self.location[1] - 1)
        if direction == "^":
            self.location = (self.location[0], self.location[1] + 1)
        if direction == "<":
            self.location = (self.location[0] - 1, self.location[1])


def part1(data):
    """Solve part 1"""
    santa = Sleigh()
    for direction in data:
        santa.drive_to_next_house(direction)
        santa.visit_house()

    return len(santa.houses_visited.keys())


def part2(data):
    """Solve part 2"""
    santa = Sleigh()
    robot = Sleigh()
    for index, direction in enumerate(data):
        if index % 2 == 0:
            santa.drive_to_next_house(direction)
            santa.visit_house()
        else:
            robot.drive_to_next_house(direction)
            robot.visit_house()

    # Merge houses visited
    houses_visited = set(santa.houses_visited.keys()).union(
        set(robot.houses_visited.keys())
    )

    return len(houses_visited)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    # Connect to the API
    puzzle_input = Puzzle(year=2015, day=3).input_data
    # Solve
    answer1, answer2 = solve(puzzle_input)
    # Submit answers
    submit(answer1, part="a", day=3, year=2015)
    submit(answer2, part="b", day=3, year=2015)
