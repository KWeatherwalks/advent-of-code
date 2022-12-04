# test_aoc_template.py
# Modified from https://realpython.com/python-advent-of-code/#a-starting-template

import pathlib

import aoc202204 as aoc
import pytest
from aocd.models import Puzzle

PUZZLE_DIR = pathlib.Path(__file__).parent / "example-data"


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "04_example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [
        ({2,3,4}, {6,7,8}),
        ({2,3}, {4,5}),
        ({5,6,7}, {7,8,9}),
        ({2,3,4,5,6,7,8}, {3,4,5,6,7}),
        ({6}, {4,5,6}),
        ({2,3,4,5,6}, {4,5,6,7,8})]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 2


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == 4
