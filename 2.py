"""
Advent of Code 2022
Puzzle 2
"""
from helpers import getInput

ROCK, PAPER, SCISSOR = "ROCK", "PAPER", "SCISSOR"

LOST_GAMES = {ROCK: SCISSOR, PAPER: ROCK, SCISSOR: PAPER}
WON_GAMES = {ROCK: PAPER, PAPER: SCISSOR, SCISSOR: ROCK}


def get_player_movements(game, cheat):
    opponent = game[0]
    response = game[2]

    opponent_values = {"A": ROCK, "B": PAPER, "C": SCISSOR }
    response_values = {"X": ROCK, "Y": PAPER, "Z": SCISSOR }

    if opponent in opponent_values:
        opponent = opponent_values.get(opponent)

    if response in response_values:
        response = response_values.get(response)

    if cheat:
        if response == PAPER: # Y: Draw
            response = opponent
        elif response == ROCK: # X: Lose
            response = LOST_GAMES.get(opponent)
        elif response == SCISSOR: # Z: Win
            response = WON_GAMES.get(opponent)

    return opponent, response

def calculate_shape_points(player_points, movement):
    if movement == ROCK:
        player_points += 1
    elif movement == PAPER:
        player_points += 2
    elif movement == SCISSOR:
        player_points += 3

    return player_points

def calculate_victory_points(my_score, opponent, response):
    if (opponent, response) in LOST_GAMES.items():
        add_score = 0
    elif (opponent, response) in WON_GAMES.items():
        add_score = 6
    else:
        add_score = 3

    my_score += add_score

    return my_score


def game(cheat=False):
    total_points = 0

    for game in getInput(2):
        my_score = 0

        opponent, response = get_player_movements(game, cheat)

        my_score = calculate_shape_points(my_score, response)
        my_score = calculate_victory_points(my_score, opponent, response)

        total_points += my_score

    print(total_points)


def main():
    game()
    game(True)

main()
