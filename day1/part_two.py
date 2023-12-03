import re

STRING_DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_input(src: str) -> list[str]:
    codes = []
    with open(src, "r") as f:
        for line in f:
            codes.append(line.strip())
    return codes


def get_digits(code: str) -> list[int]:
    pattern = re.compile(rf'(?=(\d|{"|".join(STRING_DIGITS)}))')
    return pattern.findall(code)


def sum_digits(digits: list[str]) -> int:
    sum = 0
    if len(digits) == 1:
        sum = int(STRING_DIGITS.get(digits[0], digits[0]) * 2)
    else:
        sum = int(
            STRING_DIGITS.get(digits[0], digits[0])
            + STRING_DIGITS.get(digits[-1], digits[-1])
        )
    return sum


def get_calibration(codes: list[str]) -> int:
    calibration_sum = 0
    for code in codes:
        digits = get_digits(code)
        sum = sum_digits(digits)
        calibration_sum += sum
    return calibration_sum


def main():
    codes = get_input("input.txt")
    calibration_code = get_calibration(codes)
    print(calibration_code)


if __name__ == "__main__":
    main()

# 54076
