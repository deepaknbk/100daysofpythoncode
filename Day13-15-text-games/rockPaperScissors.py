def main():
    print_header()

def print_header():
    print('---------------------------------')
    print('      ROCK PAPER SCISSORS')
    print('---------------------------------')
    print()


def game_loop(player1, player2, rolls):
        count = 1
        while count < 3:
            p2_roll = None  # TODO: get random roll
            p1_roll = None  # TODO: have player choose a roll

            outcome = p1_roll.can_defeat(p2_roll)

            # display throws
            # display winner for this round

            count += 1

        # Compute who won

if __name__ == '__main__':
    main()