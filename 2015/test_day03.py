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
def example2():
    return aoc.parse(parse_text_file("03_example2.txt"))


@pytest.fixture
def example3():
    return aoc.parse(parse_text_file("03_example3.txt"))


@pytest.fixture
def example4():
    return aoc.parse(parse_text_file("03_example4.txt"))


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == ">"


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 2


def test_part1_example2(example2):
    """Test part 1 on example input"""
    assert aoc.part1(example2) == 4


def test_part1_example3(example3):
    """Test part 1 on example input"""
    assert aoc.part1(example3) == 2


def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc.part2(example2) == 3


def test_part2_example3(example3):
    """Test part 2 on example input"""
    assert aoc.part2(example3) == 11


def test_part2_example4(example4):
    """Test part 2 on example input"""
    assert aoc.part2(example4) == 3
