#
# Thanks to Real Python! https://realpython.com/python-advent-of-code/
# https://github.com/wimglenn/advent-of-code-data#how-does-this-library-work


from aocd import submit
from aocd.models import Puzzle

# Connect to the API
puzzle = Puzzle(year=2021, day=1)

# Pull in input data as a list of integers
numbers = [int(number) for number in puzzle.input_data.split('\n')]

# Count the number of increases
answer = sum([numbers[i+1] > numbers[i]
             for i in range(len(numbers)-1)])

# Submit answer!
submit(answer, part='a', day=1, year=2021)
