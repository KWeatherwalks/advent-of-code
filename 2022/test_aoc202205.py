# test_aoc_template.py
# Modified from https://realpython.com/python-advent-of-code/#a-starting-template

import pathlib

import aoc202205 as aoc
import pytest
from aocd.models import Puzzle

PUZZLE_DIR = pathlib.Path(__file__).parent / "example-data"


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "05_example1.txt").read_text()
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = Puzzle(year=2022, day=5).input_data
    # puzzle_input = (PUZZLE_DIR / "05_puzzleinput.txt").read_text()
    return aoc.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == (
        ['ZN', 'MCD', 'P'],
        [[1,2,1],[3,1,3],[2,2,1],[1,1,2]]
    )


def test_parse_example2(example2):
    """Test that input is parsed properly"""
    assert type(example2) == type(tuple())
    assert len(example2) == 2
    assert len(example2[0]) == 9
    assert len(example2[1]) == 502
    assert list(map(len, example2[0])) == [8,3,8,7,5,8,6,4,7]
    


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == "CMZ"



def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == "MCD"
