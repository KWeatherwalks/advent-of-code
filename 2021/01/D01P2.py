from aocd import submit
from aocd.models import Puzzle

# Connect to the API
puzzle = Puzzle(year=2021, day=1)

# Pull in input data as a list of integers
numbers = [int(number) for number in puzzle.input_data.split('\n')]

# Sliding window
prev_window_sum = sum(numbers[:3])
cur_window_sum = prev_window_sum
answer = 0

for i in range(3, len(numbers)):

    # update the current window
    cur_window_sum += numbers[i] - numbers[i-3]

    if cur_window_sum > prev_window_sum:
        answer += 1

    # update the previous window
    prev_window_sum = cur_window_sum


# Submit answer!
submit(answer, part='b', day=1, year=2021)
