from aocd import submit
from aocd.models import Puzzle

# Connect to the API
puzzle = Puzzle(year=2021, day=2)

# Pull in input data as list of tuples
instructions = [x.split() for x in puzzle.input_data.split('\n')]
instructions = [tuple([x[0], int(x[1])]) for x in instructions]

# Set initial conditions
horizontal = 0
depth = 0
aim = 0

# Evaluate the instructions
for instruction, distance in instructions:

    if instruction == 'forward':
        horizontal += distance
        depth += aim * distance

    if instruction == 'up':
        aim -= distance

    if instruction == 'down':
        aim += distance

# Calculate answer
answer = horizontal * depth

# Submit answer to AoC!
submit(answer, part='b', day=2, year=2021)
