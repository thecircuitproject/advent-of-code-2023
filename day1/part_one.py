import re


def get_input(src: str) -> list[str]:
    codes = []
    with open(src, "r") as f:
        for line in f:
            codes.append(line.strip())
    return codes


def get_digits(code: str) -> list[int]:
    return re.findall(r"\d", code)


def sum_digits(digits: list[str]) -> int:
    sum = 0
    if len(digits) == 1:
        sum = int(digits[0] * 2)
    else:
        sum = int(digits[0] + digits[-1])
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
