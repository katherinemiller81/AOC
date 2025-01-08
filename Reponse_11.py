import os
import sys
from collections import defaultdict

def get_data():
    cwd = os.getcwd()
    with open(cwd + '/Jour11_input.txt', 'r') as file:
        string_list = file.read().strip().split()
    return [int(string) for string in string_list]

def blink_part1(array):
    res = []
    for x in array:
        if x == 0:
            res.append(1)
        elif len(str(x)) % 2 == 0:
            l = len(str(x))
            res += [int(str(x)[:l//2]), int(str(x)[l//2:])]
        else:
            res += [x * 2024]
    return res

def part1():
    stones = get_data()
    blinks = 25
    for i in range(blinks):
        stones = blink_part1(stones)
    return len(stones)

sys.setrecursionlimit(2**30)


def data_to_dict(data):
    entiers = defaultdict(int)
    for x in data:
        entiers[x] += 1
    return entiers

def blink_part2(entiers):
    nouveaux_entiers = defaultdict(int)
    for x in entiers:
        l = len(str(x))
        if x == 0:
            nouveaux_entiers[1] += entiers[0]
        elif l % 2 == 0:
            nouveaux_entiers[int(str(x)[:l//2])] += entiers[x]
            nouveaux_entiers[int(str(x)[l//2:])] += entiers[x]
        else:
            nouveaux_entiers[x * 2024] += entiers[x]

    return nouveaux_entiers

def part2():
    entiers = data_to_dict(get_data())
    blinks = 75
    for i in range(blinks):
        entiers = blink_part2(entiers)

    resultat = 0
    for x in entiers:
        resultat += entiers[x]
    return resultat
