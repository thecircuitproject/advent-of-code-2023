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
        clean_card_id = re.sub(r"\s{2,3}", " ", card_id)
        parsed_cards[clean_card_id] = {
            "winning_numbers": winning_numbers,
            "numbers": numbers,
        }
    return parsed_cards


def get_winning_numbers(cards: dict[str, dict[str, list[str]]]) -> dict[str, int]:
    matching_numbers = {}
    for card_id, card in cards.items():
        winning_numbers = [
            number for number in card["winning_numbers"] if number in card["numbers"]
        ]
        matching_numbers[card_id] = len(winning_numbers)
    return matching_numbers


def scratchcards_count(matching_numbers: dict[str, int]) -> int:
    card_instances = {card_id: 0 for card_id in matching_numbers.keys()}
    for card_id, matching_number in matching_numbers.items():
        id_number = int(card_id.split(" ")[-1])
        if matching_number > 0:
            for _ in range(card_instances[card_id] + 1):
                for n in range(id_number, matching_number + id_number):
                    card_instances[f"Card {n + 1}"] += 1
        card_instances[card_id] += 1
    return card_instances


def total_scratchcards(card_instances: dict[str, int]) -> int:
    return sum([number for number in card_instances.values()])


def main():
    cards = get_input()
    parsed_cards = parse_cards(cards)
    matching_numbers = get_winning_numbers(parsed_cards)
    card_instances = scratchcards_count(matching_numbers)
    total = total_scratchcards(card_instances)
    print(total)


if __name__ == "__main__":
    main()
