import sys


def get_input():
    # Read input from stdin
    puzzle_input = open("input.txt","r").read().strip().split("\n")
    return puzzle_input


def part1(input):
    result = 0
    for number in input:
        result += int(float(number)/3) -2
    
    return result


def part2(input):
    result = 0
    for number in input:
        result += calcFuel(number)
    return result
    
def calcFuel(number):
    calculatedFuel = int(float(number)/3) -2
    if calculatedFuel <=0:
        return 0
    return calculatedFuel + calcFuel(calculatedFuel)

print(part2(get_input()))
