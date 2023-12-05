from pprint import pprint
import re


def get_input(src: str = "input.txt") -> list[str]:
    cards = []
    with open(src, "r") as f:
        for line in f:
            cards.append(line.strip())
    return cards


def parse_cards(cards: list[str]) -> dict[str, dict[str, list]]:
    parsed_cards = {}
    for card in cards:
        card_id, card_numbers = card.split(": ")
        winning_numbers = re.findall(r"\d+", card_numbers.split(" | ")[0])
        numbers = re.findall(r"\d+", card_numbers.split(" | ")[-1])
        parsed_cards[card_id] = {"winning_numbers": winning_numbers, "numbers": numbers}
    return parsed_cards


def get_winning_numbers(cards: dict[str, dict[str, list[str]]]) -> dict[str, list[str]]:
    matching_numbers = {}
    for card_id, card in cards.items():
        winning_numbers = [
            number for number in card["winning_numbers"] if number in card["numbers"]
        ]
        matching_numbers[card_id] = winning_numbers
    return matching_numbers


def calculate_points(matching_numbers: dict[str, list[str]]) -> int:
    points = 0
    for card_id, winning in matching_numbers.items():
        if winning:
            points += 2 ** (len(winning) - 1)
    return points


def main():
    cards = get_input()
    parsed_cards = parse_cards(cards)
    matching_numbers = get_winning_numbers(parsed_cards)
    result = calculate_points(matching_numbers)
    print(result)


if __name__ == "__main__":
    main()
