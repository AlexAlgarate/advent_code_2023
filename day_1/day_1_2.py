import re
from typing import Dict, List

DICT_NUMBERS: Dict[str, int] = {
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


def open_file(file: str) -> str:
    return open(file).read().splitlines()


def get_calibration(file: List[str]) -> int:
    calibration = 0
    for line in file:
        digits = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
        value = "".join([DICT_NUMBERS[d] if d.isalpha() else d for d in [digits[0], digits[-1]]])
        calibration += int(value)


file = open_file(file="input_2.txt")
print("Day 01 Part 2:", get_calibration(file=file))
