import os

def get_data():
    cwd = os.getcwd()
    with open(cwd + '/Jour15_input.txt', 'r') as file:
        data = file.read().strip()
    s1, s2 = data.split("\n\n")
    grid = [list(line) for line in s1.split("\n")]
    steps = s2.replace("\n", "")
    return grid, steps

def in_grid_part1(n, i, j):
    return (0 <= i < n) and (0 <= j < n)

def move_part1(direction, n, ci, cj, grid):
    newi, newj = ci + direction[0], cj + direction[1]
    if not in_grid_part1(n, newi, newj):
        return (ci, cj, grid)

    # If is box, try pushing box
    di, dj = ci, cj
    while in_grid_part1(n, di, dj):
        di += direction[0]
        dj += direction[1]
        if not in_grid_part1(n, di, dj):
            break

        if grid[di][dj] == "#":
            break

        if grid[di][dj] == ".":
            grid[di][dj] = "O"
            grid[ci][cj] = "."
            ci, cj = ci+direction[0], cj+direction[1]
            grid[ci][cj] = "@"
            break
    return (ci, cj, grid)

def part1():
    grid, steps = get_data()
    n = len(grid)
    dirs = {
        "<": [0, -1],
        "v": [1, 0],
        ">": [0, 1],
        "^": [-1, 0]
    }
    ci, cj = 0, 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "@":
                ci, cj = i, j
                break

    for step in steps:
        ci, cj, grid = move_part1(dirs[step], n, ci, cj, grid)

    ans = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "O":
                ans += (100*i + j)
    return ans

def in_grid_part2(n, i, j):
    return (0 <= i < n) and (0 <= j < 2*n)

def move_part2(direction, n, ci, cj):
    newi, newj = ci + direction[0], cj + direction[1]
    if not in_grid_part2(n, newi, newj):
        return ci, cj

    if [newi, newj] in walls:
        return ci, cj

    stack = []
    if [newi, newj] in boxes:
        stack.append([newi, newj])
    if [newi, newj-1] in boxes:
        stack.append([newi, newj-1])

    # Determine dependencies
    can_move = True

    seen = set()
    while len(stack) > 0:
        topi, topj = stack.pop()
        ni, nj = topi + direction[0], topj + direction[1]
        if not in_grid_part2(n, ni, nj):
            can_move = False
            break

        if [ni, nj] in walls or [ni, nj+1] in walls:
            can_move = False
            break

        if (topi, topj) in seen:
            continue
        seen.add((topi, topj))

        if [ni, nj] in boxes:
            stack.append([ni, nj])
        if [ni, nj-1] in boxes:
            stack.append([ni, nj-1])
        if [ni, nj+1] in boxes:
            stack.append([ni, nj+1])

    if not can_move:
        return ci, cj

    # Can move, hooray!
    for i, box in enumerate(boxes):
        if tuple(box) in seen:
            boxes[i][0] += direction[0]
            boxes[i][1] += direction[1]

    ci += direction[0]
    cj += direction[1]

    return ci, cj

def part2():
    global grid, boxes, walls
    grid, steps = get_data()
    n = len(grid)
    dirs = {
        "<": [0, -1],
        "v": [1, 0],
        ">": [0, 1],
        "^": [-1, 0]
    }
    boxes = []
    walls = []
    ci, cj = 0, 0

    for i in range(n):
        for j in range(n):
            if grid[i][j] == "@":
                ci, cj = i, j*2
            elif grid[i][j] == "O":
                boxes.append([i, j*2])
            elif grid[i][j] == "#":
                walls.append([i, j*2])
                walls.append([i, j*2+1])

    for step in steps:
        ci, cj = move_part2(dirs[step], n, ci, cj)

    ans = 0
    for i, j in boxes:
        ans += i*100 + j

    return ans

def print_grid(boxes, walls, ci, cj):
    for i in range(n):
        for j in range(n*2):
            if [i, j] in walls:
                print("#", end="")
            elif [i, j] in boxes:
                print("[", end="")
            elif [i, j-1] in boxes:
                print("]", end="")
            elif (i, j) == (ci, cj):
                print("@", end="")
            else:
                print(".", end="")
        print()
