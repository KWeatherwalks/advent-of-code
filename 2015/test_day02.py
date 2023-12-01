# test_aoc_template.py
# Modified from https://realpython.com/python-advent-of-code/#a-starting-template

import pathlib

import day02 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent / "example-data"


def txt_to_string(filename):
    """Helper function to keep fixture functions DRY"""
    return (PUZZLE_DIR / filename).read_text().strip()


# Fixtures
@pytest.fixture
def example1():
    puzzle_input = txt_to_string("02_example1.txt")
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = txt_to_string("02_example2.txt")
    return aoc.parse(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = txt_to_string("02_example3.txt")
    return aoc.parse(puzzle_input)


# Tests


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    expected = ["2x3x4"]
    assert type(example1) == type(expected)
    assert example1 == expected


# Part 1


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 58


def test_part1_example2(example2):
    """Test part 1 on example input"""
    assert aoc.part1(example2) == 43


def test_part1_example3(example3):
    """Test part 1 on example input"""
    assert aoc.part1(example3) == 58 + 43


# Part 2


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == 34


def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc.part2(example2) == 14


def test_part2_example3(example3):
    """Test part 2 on example input"""
    assert aoc.part2(example3) == 34 + 14
