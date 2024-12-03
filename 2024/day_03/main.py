import dotenv
import os
import requests
import re
import functools

dotenv.load_dotenv("../../.env")

INPUT_FILENAME = os.getenv("INPUT_FILENAME")
SESSION_COOKIE = os.getenv("SESSION_COOKIE")
EVENT = 2024
DAY = 3
URL = f"https://adventofcode.com/{EVENT}/day/{DAY}/input"
HEADERS = {"Cookie": f"session={SESSION_COOKIE}"}

def get_input():
    chall_input = None
    if not os.path.isfile(INPUT_FILENAME):
        r = requests.get(URL, headers=HEADERS)
        if r.status_code == 200:
            with open(INPUT_FILENAME, "w") as file:
                file.write(r.text)
    with open(INPUT_FILENAME, "r") as file:
        chall_input = file.read().strip()
    return chall_input

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
    # part_1()
    # part_2()
