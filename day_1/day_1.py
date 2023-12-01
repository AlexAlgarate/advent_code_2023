from typing import List


def combin_digits(x: List[str]) -> int:
    if not x or not any(c.isdigit() for c in x):
        return 0
    digits: List[str] = [int(c) for c in x if c.isdigit()]
    return int(digits[0] + digits[-1])


def open_file(filename: str) -> List[str]:
    with open(filename, 'r') as file:
        return file.read().splitlines()


line = open_file('input.txt')
print(type(line))

result = sum(list(map(combin_digits, line)))
print(result)
