import os

def get_data():
    cwd = os.getcwd()
    with open(cwd + '/Jour9_input.txt', 'r') as file:
        data = file.read().strip()
    return data

def make_filesystem_part1(data):
    blocks = []
    is_file = True
    id_elt = 0
    for x in data:
        x = int(x)
        if is_file:
            blocks += [id_elt] * x
            id_elt += 1
            is_file = False
        else:
            blocks += [None] * x
            is_file = True

    return blocks

def move_part1(array):
    first_free = 0
    while array[first_free] != None:
        first_free += 1

    i = len(array) - 1
    while array[i] == None:
        i -= 1

    while i > first_free:
        array[first_free] = array[i]
        array[i] = None
        while array[i] == None:
            i -= 1
        while array[first_free] != None:
            first_free += 1

    return array

def part1():
    filesystem = make_filesystem_part1(get_data())
    new_array = move_part1(filesystem)
    checksum = 0
    for i, x in enumerate(new_array):
        if x != None:
            checksum += i * x
    return checksum

def make_filesystem_part2(line):
    global loc, size
    size = [0] * len(line)
    loc = [0] * len(line)

    blocks = []
    is_file = True
    id = 0
    for x in line:
        x = int(x)
        if is_file:
            loc[id] = len(blocks)
            size[id] = x
            blocks += [id] * x
            id += 1
            is_file = False
        else:
            blocks += [None] * x
            is_file = True

    return blocks

def move_part2(array):
    # Current file to move
    big = 0
    while size[big] > 0:
        big += 1
    big -= 1

    for to_move in range(big, -1, -1):
        # Find first free space that works
        free_space = 0
        first_free = 0
        while first_free < loc[to_move] and free_space < size[to_move]:
            first_free = first_free + free_space
            free_space = 0
            while array[first_free] != None:
                first_free += 1
            while first_free + free_space < len(array) and array[first_free + free_space] == None:
                free_space += 1

        if first_free >= loc[to_move]:
            continue

        # Move file by swapping block values
        for idx in range(first_free, first_free + size[to_move]):
            array[idx] = to_move
        for idx in range(loc[to_move], loc[to_move] + size[to_move]):
            array[idx] = None

    return array

def part2():
    filesystem = make_filesystem_part2(get_data())
    new_array = move_part2(filesystem)
    checksum = 0
    for i, x in enumerate(new_array):
        if x != None:
            checksum += i * x
    return checksum
