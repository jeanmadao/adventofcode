import dotenv
import os
import requests

dotenv.load_dotenv("../../.env")

INPUT_FILENAME = os.getenv("INPUT_FILENAME")
SESSION_COOKIE = os.getenv("SESSION_COOKIE")
EVENT = 2024
DAY = 2
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
    for line in chall_input.split('\n'):
        report = [int(value) for value in line.split()]
        report_len = len(report)
        safe = True
        direction = 1 if report[0] < report[1] else -1
        i = 1
        while safe and i < report_len:
            if not 1 <= (report[i] - report[i - 1]) * direction <= 3:
                safe = False
            i += 1
        if safe:
            res += 1
    print(f"{res = }")
    return res

def part_2():
    chall_input = get_input()
    res = 0 
    for line in chall_input.split('\n'):
        report = [int(value) for value in line.split()]
        error_count = 0
        safe = True
        asc = desc = eq = 0
        for i in range(1, len(report)):
            if report[i] > report[i - 1]:
                asc += 1
            elif report[i] < report[i - 1]:
                desc += 1
            else:
                eq += 1
        if min(asc, desc) + eq <= 1:
            direction = 1 if asc > desc else -1
            i = 1
            while safe and i < len(report):
                if not 1 <= (report[i] - report[i - 1]) * direction <= 3:
                    error_count += 1
                    if error_count > 1:
                        safe = False
                    elif (not i + 1 < len(report) or 1 <= (report[i + 1] - report[i]) * direction <= 3) and (not i - 2 >= 0 or 1 <= (report[i] - report[i - 2]) * direction <= 3):
                        report.pop(i - 1)
                    else:
                        report.pop(i)
                    i = max(1, i - 1)
                else:
                    i += 1
        else:
            safe = False
        if safe:
            res += 1
    print(f"{res = }")
    return res 

if __name__ == "__main__":
    # part_1()
    part_2()
