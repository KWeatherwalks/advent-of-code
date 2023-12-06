# test_aoc_template.py
# Modified from https://realpython.com/python-advent-of-code/#a-starting-template

import pathlib

import day04 as aoc
import pytest
from aocd.models import Puzzle

PUZZLE_DIR = pathlib.Path(__file__).parent / "example-data"


def parse_text_file(filename):
    """Helper function to keep fixture functions DRY"""
    return (PUZZLE_DIR / filename).read_text().strip()


@pytest.fixture
def example1():
    puzzle_input = parse_text_file("04_example1.txt")
    return aoc.parse(puzzle_input)


@pytest.mark.skip(reason="No data given")
@pytest.fixture
def example2():
    puzzle_input = parse_text_file("04_example2.txt")
    return aoc.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    ]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 13


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == 30
