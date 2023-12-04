from typing import List


def combine_digits(x: str) -> int:
    if not x or not any(c.isdigit() for c in x):
        return 0
    digits: List[str] = [number for number in x if number.isdigit()]
    return int(digits[0] + digits[-1])


def open_file(filename: str) -> None:
    try:
        return open(filename)
    except FileNotFoundError:
        print(f"File {filename} not found")
        raise


f = open_file("input_1.txt")
result = sum(map(combine_digits, f.read().splitlines()))
print(result)
