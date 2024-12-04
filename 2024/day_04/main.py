import dotenv
import os
import requests

dotenv.load_dotenv("../../.env")

INPUT_FILENAME = os.getenv("INPUT_FILENAME")
SESSION_COOKIE = os.getenv("SESSION_COOKIE")
EVENT = 2024
DAY = 4
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

    grid = chall_input.split('\n')
    height = len(grid)
    width = len(grid[0])
    target_word = "XMAS"
    len_word = len(target_word)

    for i in range(height):
        for j in range(width):
            for dir in [(0, 1), (1, 1), (1, 0), (1, -1)]:
                if 0 <= i + (len_word - 1) * dir[0] < height and 0 <= j + (len_word - 1) * dir[1] < width:
                    word = "".join([grid[i + k * dir[0]][j + k * dir[1]] for k in range(len_word)])
                    if word in [target_word, target_word[::-1]]:
                        res += 1
    print(f"{res = }")
    return res

def part_2():
    chall_input = get_input()
    res = 0 

    grid = chall_input.split('\n')
    height = len(grid)
    width = len(grid[0])
    target_word = "MAS"
    len_word = len(target_word)

    for i in range(height - len_word + 1):
        for j in range(width - len_word + 1):
            if 0 <= i + len_word - 1 < height and 0 <= j + len_word - 1 < width:
                first_word = "".join([grid[i + k][j + k] for k in range(len_word)])
                if first_word in [target_word, target_word[::-1]]:
                    second_word = "".join([grid[i + len_word - 1 - k][j + k] for k in range(len_word)])
                    if second_word in [target_word, target_word[::-1]]:
                        res += 1
    print(f"{res = }")
    return res 

if __name__ == "__main__":
    # part_1()
    part_2()
