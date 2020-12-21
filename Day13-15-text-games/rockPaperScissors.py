"""found code over internet """
from players import Player, Roll
import random


def print_header():
    print('---------------------------')
    print('--- Rock Paper Scissors ---')
    print('---------------------------')


def build_rolls():
    paper = Roll('paper')
    rock = Roll('rock')
    scissors = Roll('scissors')
    rolls = [paper, rock, scissors]

    return rolls


def get_players_name():
    name = input("Please enter your name: ").capitalize()
    return name


def get_player_roll():
    inp = input("Please choose a roll: [r]ock, [p]aper, or [s]cissors  ")

    if inp == 'r':
        return Roll('rock')

    elif inp == 'p':
        return Roll('paper')

    elif inp == 's':
        return Roll('scissors')


def game_loop(player1, player2, rolls):
    count = 0
    while count < 3:
        print(f"Starting round {count+1}")
        p1_roll = get_player_roll()
        p2_roll = random.choice(rolls)

        # display throws
        print(f"Player 1 throw: {p1_roll.name}")
        print(f"Player 2 throw: {p2_roll.name}")

        # Check for tie
        if p1_roll.name == p2_roll.name:
            print("Tie! We will have to re-do this round.")
            continue

        # Check for winner
        p1_win = p1_roll.can_defeat(p2_roll)

        # display winner for this round
        if p1_win:
            print(f'{player1.name} wins this round with {p1_roll.name} defeating {p2_roll.name}')
            player1.score += 1

        else:
            print(f'{player2.name} wins this round with {p2_roll.name} defeating {p1_roll.name}')
            player2.score += 1

        count += 1

        # Compute who won
        if player1.score == 2:
            print(f"{player1.name} is the winner by winning {player1.score} to {player2.score}")
            break

        if player2.score == 2:
            print(f"{player2.name} is the winner by winning {player2.score} to {player1.score}")
            break


def main():
    print_header()

    rolls = build_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("Bill the Computer")

    game_loop(player1, player2, rolls)


if __name__ == '__main__':
    main()