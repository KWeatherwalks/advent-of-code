# test_aoc_template.py
# Modified from https://realpython.com/python-advent-of-code/#a-starting-template

import pathlib

import aoc_template as aoc
import pytest
from aocd.models import Puzzle

PUZZLE_DIR = pathlib.Path(__file__).parent / "example-data"


def parse_text_file(filename):
    """Helper function to keep fixture functions DRY"""
    return (PUZZLE_DIR / filename).read_text().strip()


@pytest.fixture
def example1():
    puzzle_input = parse_text_file("example1.txt")
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = parse_text_file("example2.txt")
    return aoc.parse(puzzle_input)


@pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == ...


@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == ...
