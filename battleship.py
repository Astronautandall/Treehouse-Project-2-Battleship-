import random

# Utilities
from constants import Constants
from handler import Handler

# Classes
from player import Player
from board import Board
from ship import Ship
from position import Position


def main():

    Handler.clear_screen()

    print('Welcome to the Battleship game!')
    input('Press ENTER to start playing')
    Handler.clear_screen()

    player1 = Player('Player 1, what is your name?')
    Handler.clear_screen()

    player2 = Player('Player 2, would you kindly write your name:')
    Handler.clear_screen()

    player1.set_fleet()
    Handler.clear_screen()

    player2.set_fleet()
    Handler.clear_screen()

    input("All set. LET'S PLAY!\nPress ENTER to continue")

    Handler.clear_screen()

    while True:

        player1.turn(player2)
        if not player2.has_live_ships():
            print('{} WINS!'.format(player1.name))
            break

        player2.turn(player1)
        if not player1.has_live_ships():
            print('{} WINS!'.format(player2.name))
            break

    # Printing a blank space
    print()
    Board.print_final_boards(player1, player2)


# Make sure the script doesn't execute when imported
# All of the logic and function should be called in
# __name__ == "__main__": block.
if __name__ == '__main__':

    main()
