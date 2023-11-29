# test_aoc_template.py
# Modified from https://realpython.com/python-advent-of-code/#a-starting-template

import pathlib

import day01 as aoc
import pytest
from aocd.models import Puzzle

PUZZLE_DIR = pathlib.Path(__file__).parent / "example-data"


def parse_text_file(filename):
    """Helper function to keep fixture functions DRY"""
    return (PUZZLE_DIR / filename).read_text().strip()


# Fixtures
@pytest.fixture
def example1():
    puzzle_input = parse_text_file("example1.txt")
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = parse_text_file("example2.txt")
    return aoc.parse(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = parse_text_file("example3.txt")
    return aoc.parse(puzzle_input)


@pytest.fixture
def example4():
    puzzle_input = parse_text_file("example4.txt")
    return aoc.parse(puzzle_input)


@pytest.fixture
def example5():
    puzzle_input = parse_text_file("example5.txt")
    return aoc.parse(puzzle_input)


@pytest.fixture
def example6():
    puzzle_input = parse_text_file("example6.txt")
    return aoc.parse(puzzle_input)


@pytest.fixture
def example7():
    puzzle_input = parse_text_file("example7.txt")
    return aoc.parse(puzzle_input)


@pytest.fixture
def example8():
    puzzle_input = parse_text_file("example8.txt")
    return aoc.parse(puzzle_input)


@pytest.fixture
def example9():
    puzzle_input = parse_text_file("example9.txt")
    return aoc.parse(puzzle_input)


# Tests


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    expected = "(())"
    assert example1 == expected


# Part 1


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 0


def test_part1_example2(example2):
    """Test part 1 on example input"""
    assert aoc.part1(example2) == 0


def test_part1_example3(example3):
    """Test part 1 on example input"""
    assert aoc.part1(example3) == 3


def test_part1_example4(example4):
    """Test part 1 on example input"""
    assert aoc.part1(example4) == 3


def test_part1_example5(example5):
    """Test part 1 on example input"""
    assert aoc.part1(example5) == 3


def test_part1_example6(example6):
    """Test part 1 on example input"""
    assert aoc.part1(example6) == -1


def test_part1_example7(example7):
    """Test part 1 on example input"""
    assert aoc.part1(example7) == -1


def test_part1_example8(example8):
    """Test part 1 on example input"""
    assert aoc.part1(example8) == -3


def test_part1_example9(example9):
    """Test part 1 on example input"""
    assert aoc.part1(example9) == -3


# Part 2


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == ...
