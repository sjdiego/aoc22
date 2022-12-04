"""
Advent of Code 2022
Helpers
"""

def getInput(id: int):
    lines = []

    with open(f"./inputs/{id}.txt", "r") as file:
        for line in file:
            lines.append(line.strip())

    return lines
