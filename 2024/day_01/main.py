import dotenv
import os
import requests

dotenv.load_dotenv("../../.env")

INPUT_FILENAME = os.getenv("INPUT_FILENAME")
SESSION_COOKIE = os.getenv("SESSION_COOKIE")
EVENT = 2024
DAY = 1
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
    chall_input = get_input()
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
    # part_1()
    # part_2()
