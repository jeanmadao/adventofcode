import sys

sys.path.append("../../")
from lib import get_input

EVENT = 2024
DAY = 1

def part_1():
    chall_input = get_input(EVENT, DAY)
    res = 0 
    a = []
    b = []
    for line in chall_input.split('\n'):
        value_a, value_b = line.split()
        a.append(int(value_a))
        b.append(int(value_b))
    for value_a, value_b in zip(sorted(a), sorted(b)):
        res += abs(value_a - value_b)
    print(f"{res = }")
    return res


def part_2():
    chall_input = get_input(EVENT, DAY)
    res = 0 
    a = []
    b = []
    for line in chall_input.split('\n'):
        value_a, value_b = line.split()
        a.append(int(value_a))
        b.append(int(value_b))
    count = {}
    for value in b:
        count[value] = count.get(value, 0) + 1
    for value in a:
        res += value * count.get(value, 0)
    print(f"{res = }")
    return res 

if __name__ == "__main__":
    part_1()
    part_2()
