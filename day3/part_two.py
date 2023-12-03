import re
import math


def get_input(src: str = "input.txt") -> list[str]:
    codes = []
    with open(src, "r") as f:
        for line in f:
            codes.append(line.strip())
    return codes


def gear_ratios_sum(data: list[str]) -> int:
    numbers, symbols = parse_input(data)
    sum = 0

    for position, symbol in symbols.items():
        if symbol == "*":
            row, column = position
            adj_position = [
                (row + x, column + y) for x in [-1, 0, 1] for y in [-1, 0, 1]
            ]
            adj_numbers = set(
                [numbers[position] for position in adj_position if position in numbers]
            )
            if len(adj_numbers) == 2:
                sum += math.prod([item[0] for item in adj_numbers])

    return sum


def parse_input(data: list[str]) -> tuple[dict, dict]:
    numbers = {}
    symbols = {}
    idx_num = 0

    for r, line in enumerate(data):
        line_numbers = re.sub(r"\D", " ", line).split()
        offset = 0
        for n in line_numbers:
            position = line.index(n, offset)
            for step in range(len(n)):
                numbers[(r, position + step)] = (int(n), idx_num)
            offset = position + len(n)
            idx_num += 1

        line_symbols = re.sub(r"[\d\.]", " ", line).split()
        offset = 0
        for sym in line_symbols:
            position = line.index(sym, offset)
            symbols[(r, position)] = sym
            offset = position + 1

    return numbers, symbols


def main():
    input = get_input()
    result = gear_ratios_sum(input)
    print(result)


if __name__ == "__main__":
    main()
