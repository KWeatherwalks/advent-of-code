# aoc_template.py
# Modified from https://realpython.com/python-advent-of-code/#a-starting-template

from dataclasses import dataclass

from aocd import submit
from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input.split("\n")


@dataclass
class Scratchcard:
    # constructor
    id: int
    winning_numbers: list[int]
    player_numbers: list[int]

    def winning_number_count(self):
        return len(set(self.winning_numbers).intersection(set(self.player_numbers)))

    def points(self):
        if (count := self.winning_number_count()) == 0:
            return 0
        else:
            return 2 ** (count - 1)


class CardCollection:
    def __init__(self):
        self.counts = {}  # {card_id: count}
        self.cards = []

    def add_card(self, card, multiple=1):
        if card not in self.cards:
            self.cards.append(card)
        self.counts[card.id] = self.counts.get(card.id, 0) + multiple

    def add_cards_won(
        self, winning_card: Scratchcard, number_of_cards_won: int, multiplier=1
    ):
        for card in self.cards[winning_card.id : winning_card.id + number_of_cards_won]:
            self.add_card(card, multiple=multiplier)

    def scatch_card(self, card, multiple=1):
        self.counts[card.id] -= multiple
        self.add_cards_won(card, card.winning_number_count(), multiplier=multiple)


def string_to_scratchcard(s):
    card_id, numbers = s.split(":")
    card_id = int(card_id.replace("Card ", ""))
    winners, player = numbers.split("|")
    winners = [int(number) for number in winners.split()]
    player = [int(number) for number in player.split()]
    return Scratchcard(card_id, winners, player)


def part1(data):
    """Solve part 1"""
    total = 0
    for line in data:
        card = string_to_scratchcard(line)
        total += card.points()

    return total


def part2(data):
    """Solve part 2"""
    scratchcard_count = 0
    # Create a dictionary, key-card.id : value-count
    scratchcard_collection = CardCollection()

    # Create scratchcard collection using original set
    for line in data:
        card = string_to_scratchcard(line)
        scratchcard_collection.add_card(card)

    # iteratively move through the list scratching cards
    for card in scratchcard_collection.cards:
        duplicate_count = scratchcard_collection.counts[card.id]
        scratchcard_collection.scatch_card(card, duplicate_count)
        scratchcard_count += duplicate_count

    return scratchcard_count


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    # Connect to the API
    puzzle_input = Puzzle(year=2023, day=4).input_data
    # Solve
    answer1, answer2 = solve(puzzle_input)
    # Submit answers
    # submit(answer1, part="a", day=4, year=2023)
    # submit(answer2, part="b", day=4, year=2023)
