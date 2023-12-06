# test_aoc_template.py
# Modified from https://realpython.com/python-advent-of-code/#a-starting-template

import pathlib

import day03 as aoc
import pytest
from aocd.models import Puzzle

PUZZLE_DIR = pathlib.Path(__file__).parent / "example-data"


def parse_text_file(filename):
    """Helper function to keep fixture functions DRY"""
    return (PUZZLE_DIR / filename).read_text().strip()


@pytest.fixture
def example1():
    return aoc.parse(parse_text_file("03_example1.txt"))


@pytest.fixture
def puzzle_input():
    return aoc.parse(parse_text_file("03_puzzle_input.txt"))


@pytest.fixture
def example2():
    return aoc.parse(parse_text_file("03_puzzle_input.txt"))[:5]


def test_get_part_numbers(example2):
    assert aoc.get_part_numbers(example2, 2, 13) == [662, 360]
    assert aoc.get_part_numbers(example2, 2, 48) == [805, 677]
    assert aoc.get_part_numbers(example2, 2, 62) == [862, 780]


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert len(example1) == 12
    assert len(example1[0]) == 12
    assert example1 == [
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "4", "6", "7", ".", ".", "1", "1", "4", ".", ".", "."],
        [".", ".", ".", ".", "*", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "3", "5", ".", ".", "6", "3", "3", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", "."],
        [".", "6", "1", "7", "*", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "+", ".", "5", "8", ".", "."],
        [".", ".", ".", "5", "9", "2", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "7", "5", "5", ".", "."],
        [".", ".", ".", ".", "$", ".", "*", ".", ".", ".", ".", "."],
        [".", ".", "6", "6", "4", ".", "5", "9", "8", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 4361


# part 2


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == 467835


def test_part2_puzzle_input(puzzle_input):
    assert len(puzzle_input) == 142
    assert len(puzzle_input[0]) == 142


def test_part2_example2(example2):
    assert aoc.part2(example2) == sum([662 * 360, 805 * 677, 862 * 780])
