# test_aoc_template.py
# Modified from https://realpython.com/python-advent-of-code/#a-starting-template

import pathlib

import day02 as aoc
import pytest
from aocd.models import Puzzle

PUZZLE_DIR = pathlib.Path(__file__).parent / "example-data"


def parse_text_file(filename):
    """Helper function to keep fixture functions DRY"""
    return (PUZZLE_DIR / filename).read_text().strip()


@pytest.fixture
def example1():
    return aoc.parse(parse_text_file("02_example1.txt"))


@pytest.fixture
def example2():
    return aoc.parse(parse_text_file("02_example1.txt").split("\n")[0])


@pytest.fixture
def example3():
    return aoc.parse(parse_text_file("02_example1.txt").split("\n")[1])


@pytest.fixture
def example4():
    return aoc.parse(parse_text_file("02_example1.txt").split("\n")[2])


@pytest.fixture
def example5():
    return aoc.parse(parse_text_file("02_example1.txt").split("\n")[3])


@pytest.fixture
def example6():
    return aoc.parse(parse_text_file("02_example1.txt").split("\n")[4])


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]


def test_parse_example2(example2):
    """Test that input is parsed properly"""
    assert example2 == ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 8


def test_part1_example2(example2):
    """Test part 1 on example input"""
    assert aoc.part1(example2) == 1


def test_part1_example3(example3):
    """Test part 1 on example input"""
    assert aoc.part1(example3) == 2


def test_part1_example4(example4):
    """Test part 1 on example input"""
    assert aoc.part1(example4) == 0


def test_part1_example5(example5):
    """Test part 1 on example input"""
    assert aoc.part1(example5) == 0


def test_part1_example6(example6):
    """Test part 1 on example input"""
    assert aoc.part1(example6) == 5


# part 2


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == 2286


def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc.part2(example2) == 48


def test_part2_example3(example3):
    """Test part 2 on example input"""
    assert aoc.part2(example3) == 12


def test_part2_example4(example4):
    """Test part 2 on example input"""
    assert aoc.part2(example4) == 1560


def test_part2_example5(example5):
    """Test part 2 on example input"""
    assert aoc.part2(example5) == 630


def test_part2_example6(example6):
    """Test part 2 on example input"""
    assert aoc.part2(example6) == 36
