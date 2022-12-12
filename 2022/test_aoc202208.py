# test_aoc_template.py
# Modified from https://realpython.com/python-advent-of-code/#a-starting-template

import pathlib

import aoc202208 as aoc
import numpy as np
import pytest
from aocd.models import Puzzle

PUZZLE_DIR = pathlib.Path(__file__).parent / "example-data"


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "08_example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    expected = np.array([[3,0,3,7,3], [2,5,5,1,2], [6,5,3,3,2], [3,3,5,4,9], 
                        [3,5,3,9,0]])
    assert np.array_equal(example1, expected)
    assert example1.shape == expected.shape
    assert (example1 == expected).all()
    

def test_is_visible(example1):
    """Test is_visible function"""
    # top-left 5
    assert example1[1,1] == 5
    assert aoc.is_visible(1,1,example1) == True
    # top-middle 5
    assert example1[1,2] == 5
    assert aoc.is_visible(1,2,example1) == True
    # top-right 1
    assert example1[1,3] == 1
    assert aoc.is_visible(1,3,example1) == False
    # left-middle 5
    assert example1[2,1] == 5
    assert aoc.is_visible(2,1,example1) == True
    # center 3
    assert example1[2,2] == 3
    assert aoc.is_visible(2,2,example1) == False
    # right-middle 3
    assert example1[2,3] == 3
    assert aoc.is_visible(2,3,example1) == True


def test_count_trees(example1):
    """Test counting function"""
    assert aoc.count_trees(5,np.array([3,3])) == 2
    assert aoc.count_trees(5,np.array([4,9])) == 2
    assert aoc.count_trees(5,np.array([3,5,3])) == 2
    assert aoc.count_trees(5,np.array([3])) == 1


def test_scenic_score(example1):
    """Test scenic score"""
    assert aoc.scenic_score(1,2,example1) == 4
    assert aoc.scenic_score(3,2,example1) == 8


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 21


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == 8
