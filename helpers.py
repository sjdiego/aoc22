"""
Advent of Code 2022
Helpers
"""

def getInput(id: int) -> list:
    with open(f"./inputs/{id}.txt") as file:
        return list(map(lambda line: line.strip(), file))
