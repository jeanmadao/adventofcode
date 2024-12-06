import sys

sys.path.append("../../")
from lib import get_input

EVENT = 2024
DAY = 3

def part_1():
    chall_input = get_input()
    res = 0 
    regex = r"mul\(\d+,\d+\)"
    for operation in re.findall(regex, chall_input):
        first_digit, second_digit = operation[4:-1].split(",")
        res += int(first_digit) * int(second_digit)
    print(f"{res = }")
    return res

def part_2():
    chall_input = get_input()
    res = 0 
    regex = r"mul\(\d+,\d+\)"
    i = 0
    while i != -1:
        j = chall_input.find("don't()", i)
        if j == -1:
            searchstr = chall_input[i:]
            i = -1
        else:
            searchstr = chall_input[i:j]
            i = chall_input.find("do()", j + 7)
        for operation in re.findall(regex, searchstr):
            first_digit, second_digit = operation[4:-1].split(",")
            res += int(first_digit) * int(second_digit)
    print(f"{res = }")
    return res 

if __name__ == "__main__":
    part_1()
    part_2()
