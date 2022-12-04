"""
Advent of Code 2022
Puzzle 3
"""
from helpers import getInput

def getPriorities(lines: list) -> list:
    def convertPriority(char: str) -> str:
        c = 38 if char.isupper() else 96
        return ord(char) - c

    return list(map(
        lambda line: list(map(
            lambda char: convertPriority(char), line
        )), lines
    ))

def getCompartments(rucksacks: list) -> list:
    compartments = list()
    for compartment in rucksacks:
        chunk = list()
        half = int(len(compartment) / 2)
        for i in range(0, len(compartment), half):
            chunk.append(compartment[i:i+half])
        compartments.append(chunk)
    return compartments

def getSum(rucksacks: list) -> list:
    return sum(list(map(
        lambda backsack: list(set(backsack[0]) & set(backsack[1]))[0], rucksacks
    )))

print(getSum(getCompartments(getPriorities(getInput(3)))))
