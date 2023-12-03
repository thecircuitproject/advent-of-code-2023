import re


def get_input(src: str = "input.txt") -> list[str]:
    codes = []
    with open(src, "r") as f:
        for line in f:
            codes.append(line.strip())
    return codes


def validate_symbols(symbols: list[str]) -> bool:
    valid = True
    if all([char == "." for char in symbols]):
        valid = False
    return valid


def get_numbers(input: list[str]) -> list[str]:
    numbers = []
    for i, line in enumerate(input):
        matches = re.finditer(r"\d+", line)
        # First Row
        if i == 0:
            for number in matches:
                symbols = []
                lower = number.span()[0]
                upper = number.span()[-1] - 1
                if lower != 0:
                    # First
                    symbols.append(line[lower - 1])
                    symbols.append(input[i + 1][lower - 1])
                symbols.append(input[i + 1][lower])
                # Last
                if upper != len(line) - 1:
                    symbols.append(line[upper + 1])
                    symbols.append(input[i + 1][lower + 1])
                symbols.append(input[i + 1][lower])
                # Middle
                symbols.append(input[i + 1][lower + 1])
                if validate_symbols(symbols):
                    numbers.append(number.group())
        # Last row
        elif i == len(input) - 1:
            for number in matches:
                symbols = []
                lower = number.span()[0]
                upper = number.span()[-1] - 1
                if lower != 0:
                    # First
                    symbols.append(input[i - 1][lower - 1])
                    symbols.append(line[lower - 1])
                symbols.append(input[i - 1][lower])
                if upper != len(line) - 1:
                    # Last
                    symbols.append(input[i - 1][upper + 1])
                    symbols.append(line[upper + 1])
                symbols.append(input[i - 1][upper])
                # Middle
                symbols.append(input[i - 1][lower + 1])
                if validate_symbols(symbols):
                    numbers.append(number.group())
        # In between
        else:
            for number in matches:
                symbols = []
                lower = number.span()[0]
                upper = number.span()[-1] - 1
                if lower != 0:
                    # First
                    symbols.append(input[i - 1][lower - 1])
                    symbols.append(input[i + 1][lower - 1])
                    symbols.append(line[lower - 1])
                symbols.append(input[i - 1][lower])
                symbols.append(input[i + 1][lower])

                if upper != len(line) - 1:
                    symbols.append(input[i - 1][upper + 1])
                    symbols.append(line[upper + 1])
                    symbols.append(input[i + 1][upper + 1])

                symbols.append(input[i - 1][upper])
                symbols.append(input[i + 1][upper])
                # Middle
                symbols.append(input[i + 1][lower + 1])
                symbols.append(input[i - 1][lower + 1])
                if validate_symbols(symbols):
                    numbers.append(number.group())


def calculate_sum(numbers: list[str]) -> int:
    return sum([int(number) for number in numbers])


def main():
    input = get_input()
    numbers = get_numbers(input)
    result = calculate_sum(numbers)
    print(result)


if __name__ == "__main__":
    main()
