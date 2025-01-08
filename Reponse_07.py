import os
import itertools

def get_data():
    cwd = os.getcwd()
    with open(cwd + '/Jour7_input.txt', 'r') as file:
        lines = file.readlines()

    equations = []
    for line in lines:
        target, numbers = line.strip().split(":")
        target = int(target.strip())
        numbers = list(map(int, numbers.strip().split()))
        equations.append((target, numbers))
    return equations

def eval_combo_part_1(combo, numbers):
    resultat = numbers[0]
    for index in range(0, len(numbers) - 1):
        if combo[index] == "+":
            resultat += numbers[index + 1]
        elif combo[index] == "*":
            resultat *= numbers[index + 1]
    return resultat

def part1():
    equations = get_data()
    total_calibration_result = 0
    for target, numbers in equations:
        for combo in itertools.product("*+", repeat=len(numbers)-1):
            if eval_combo_part_1(combo, numbers) == target:
                total_calibration_result += target
                break
    return total_calibration_result

def eval_combo_part_2(combo, numbers):
    resultat = numbers[0]
    for index in range(0, len(numbers) - 1):
        if combo[index] == "+":
            resultat += numbers[index + 1]
        elif combo[index] == "*":
            resultat *= numbers[index + 1]
        elif combo[index] == "|":
            resultat = int(str(resultat) + str(numbers[index + 1]))
    return resultat

def part2():
    equations = get_data()
    total_calibration_result = 0
    for target, numbers in equations:
        for combo in itertools.product("*+|", repeat=len(numbers)-1):
            if eval_combo_part_2(combo, numbers) == target:
                total_calibration_result += target
                break
    return total_calibration_result
