import sys

sys.path.append("../../")
from lib import get_input

EVENT = 2024
DAY = 6

def part_1():
    chall_input = get_input(EVENT, DAY)
    res = 0 

    grid = chall_input.split('\n')
    height = len(grid)
    width = len(grid[0])

    start = None
    i = 0
    while not start:
        j = 0
        while not start and j < len(grid[0]):
            if grid[i][j] not in ['.', '#']:
                start = (i, j)
            j += 1
        i += 1

    loc_dict = {}

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    match grid[start[0]][start[1]]:
        case '^':
            dir_index = 0
        case '>':
            dir_index = 1
        case 'v':
            dir_index = 2
        case '<':
            dir_index = 3
        case _:
            dir_index = -1

    curr = start
    run = True

    while run:

        i, j = curr
        dir = dirs[dir_index]
        loc_id = i * width + j
        loc_dirs = loc_dict.get(loc_id, 0)

        if (loc_dirs & 2**dir_index) == 0:
            loc_dict[loc_id] = loc_dirs | 2**dir_index

            if 0 <= i + dir[0] < height and 0 <= j + dir[1] < width:
                while grid[i + dir[0]][j + dir[1]] == '#':
                    dir_index = (dir_index + 1) % 4
                    dir = dirs[dir_index]
                curr = (i + dir[0], j + dir[1])
            else:
                run = False
        else:
            run = False

    res = len(loc_dict.values())

    print(f"{res = }")
    return res

def part_2():
    chall_input = get_input(EVENT, DAY)
    res = 0 

    grid = [list(row) for row in chall_input.split('\n')]
    height = len(grid)
    width = len(grid[0])

    start = None
    i = 0
    while not start:
        j = 0
        while not start and j < len(grid[0]):
            if grid[i][j] not in ['.', '#']:
                start = (i, j)
            j += 1
        i += 1


    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    match grid[start[0]][start[1]]:
        case '^':
            start_dir_index = 0
        case '>':
            start_dir_index = 1
        case 'v':
            start_dir_index = 2
        case '<':
            start_dir_index = 3
        case _:
            start_dir_index = -1

    for i in range(height):
        for j in range(width):
            if grid[i][j] == '.':
                grid[i][j] = '#'
                loc_dict = { start[0] * width + start[1]: 2**start_dir_index }
                dir_index = start_dir_index
                run = True

                k, l = start
                while run:
                    dir = dirs[dir_index]

                    if 0 <= k + dir[0] < height and 0 <= l + dir[1] < width:
                        while grid[k + dir[0]][l + dir[1]] == '#':
                            dir_index = (dir_index + 1) % 4
                            dir = dirs[dir_index]

                        k, l = (k + dir[0], l + dir[1])
                        loc_id = k * width + l
                        loc_dirs = loc_dict.get(loc_id, 0)

                        if (loc_dirs & 2**dir_index) == 0:
                            loc_dict[loc_id] = loc_dirs | 2**dir_index

                        else:
                            run = False
                            res += 1
                    else:
                        run = False

                grid[i][j] = '.'

    print(f"{res = }")
    return res 

if __name__ == "__main__":
    part_1()
    part_2()
