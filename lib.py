import dotenv
import os
import requests

dotenv.load_dotenv()

INPUT_FILENAME = os.getenv("INPUT_FILENAME") or "input.txt"
SESSION_COOKIE = os.getenv("SESSION_COOKIE")

def get_input(event: int, day: int) -> str:
    url = f"https://adventofcode.com/{event}/day/{day}/input"
    headers = {"Cookie": f"session={SESSION_COOKIE}"}

    if not os.path.isfile(INPUT_FILENAME):
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            try:
                with open(INPUT_FILENAME, "w") as file:
                    file.write(r.text)
            except:
                raise Exception(f"Couldn't write file {INPUT_FILENAME}.")
        else:
            raise Exception(f"Could not fetch input. Status code: {r.status_code}.")

    try:
        with open(INPUT_FILENAME, "r") as file:
            chall_input = file.read().strip()
    except:
        raise Exception(f"Couldn't read file {INPUT_FILENAME}.")

    return chall_input
