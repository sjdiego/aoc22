"""
Advent of Code 2022
Puzzle 4
"""

from helpers import getInput

def getRange(elf: list) -> set:
    firstSector = int(elf.split("-")[0])
    lastSector = int(elf.split("-")[1])

    return set(range(firstSector, lastSector+1))

overlaps = 0

for section in getInput(4):
    firstElfRange = getRange(section.split(",")[0])
    secondElfRange = getRange(section.split(",")[1])

    if firstElfRange.issubset(secondElfRange) or secondElfRange.issubset(firstElfRange):
        overlaps += 1

print(overlaps)
