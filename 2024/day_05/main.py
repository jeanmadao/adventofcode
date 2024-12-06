import sys

sys.path.append("../../")
from lib import get_input

EVENT = 2024
DAY = 5

def part_1():
    chall_input = get_input(EVENT, DAY)
    res = 0 

    lines = chall_input.split('\n')
    len_lines = len(lines)
    ordering = {}

    i = 0
    while lines[i]:
        a, b = lines[i].split('|')
        ordering[a] = ordering.get(a, set()).union({b})
        i += 1
    i += 1

    for j in range(i, len_lines):
        numbers = lines[j].split(',')
        len_numbers = len(numbers)
        correct = True

        k = 0
        while correct and k < len_numbers - 1:
            if numbers[-1 - k] not in ordering.get(numbers[-2 - k], set()):
                correct = False
            k += 1
        if correct:
            res += int(numbers[len_numbers // 2])

    print(f"{res = }")
    return res

def part_2():
    chall_input = get_input(EVENT, DAY)
    res = 0 

    lines = chall_input.split('\n')
    len_lines = len(lines)
    ordering = {}

    i = 0
    while lines[i]:
        a, b = lines[i].split('|')
        ordering[a] = ordering.get(a, set()).union({b})
        i += 1
    i += 1

    for j in range(i, len_lines):
        numbers = lines[j].split(',')
        len_numbers = len(numbers)
        correct = True

        k = 0
        while k < len_numbers - 1:
            if numbers[-1 - k] not in ordering.get(numbers[-2 - k], set()):
                correct = False

                l = 1
                while -1 - k + l < len_numbers and not numbers[-1 - k + l] in ordering.get(numbers[-2 - k], set()):
                    l += 1
                numbers.insert(-1 - k + l, numbers.pop(-2 - k))
            else:
                k += 1
        if not correct:
            res += int(numbers[len_numbers // 2])

    print(f"{res = }")
    return res 

if __name__ == "__main__":
    part_1()
    part_2()
