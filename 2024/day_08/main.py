import sys

sys.path.append("../../")
from lib import get_input

EVENT = 2024
DAY = 8

def part_1():
    chall_input = get_input(EVENT, DAY)
    res = 0 

    grid = chall_input.split('\n')
    height = len(grid)
    width = len(grid[0])

    coords_dict = {}
    antinodes = set()

    for i in range(height):
        for j in range(width):
            if grid[i][j].isalnum():
                char = grid[i][j]
                coords_dict[char] = coords_dict.get(char, []) + [(i, j)]

    for key in coords_dict.keys():
        coords = coords_dict[key]
        len_coords = len(coords)
        for k in range(len_coords - 1):
            for l in range(k + 1, len_coords):
                i1, j1 = coords[k]
                i2, j2 = coords[l]
                delta_i = i1 - i2
                delta_j = j1 - j2
                if 0 <= i1 + delta_i < height and 0 <= j1 + delta_j < width:
                    antinodes.add((i1 + delta_i, j1 + delta_j))
                if 0 <= i2 - delta_i < height and 0 <= j2 - delta_j < width:
                    antinodes.add((i2 - delta_i, j2 - delta_j))

    res = len(antinodes)

    print(f"{res = }")
    return res

def part_2():
    chall_input = get_input(EVENT, DAY)
    res = 0 

    grid = chall_input.split('\n')
    height = len(grid)
    width = len(grid[0])

    coords_dict = {}
    antinodes = set()

    for i in range(height):
        for j in range(width):
            if grid[i][j].isalnum():
                char = grid[i][j]
                coords_dict[char] = coords_dict.get(char, []) + [(i, j)]

    for key in coords_dict.keys():
        coords = coords_dict[key]
        len_coords = len(coords)
        for k in range(len_coords - 1):
            for l in range(k + 1, len_coords):
                i1, j1 = coords[k]
                i2, j2 = coords[l]
                delta_i = i1 - i2
                delta_j = j1 - j2
                m = 0
                while 0 <= i1 + m*delta_i < height and 0 <= j1 + m*delta_j < width:
                    antinodes.add((i1 + m*delta_i, j1 + m*delta_j))
                    m += 1

                m = 0
                while 0 <= i1 - m*delta_i < height and 0 <= j1 - m*delta_j < width:
                    antinodes.add((i1 - m*delta_i, j1 - m*delta_j))
                    m += 1

    res = len(antinodes)

    print(f"{res = }")
    return res 

if __name__ == "__main__":
    part_1()
    part_2()
