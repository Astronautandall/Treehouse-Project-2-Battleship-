from constants import Constants
from handler import Handler

from position import Position
from ship import Ship


class Board:

    def __init__(self):

        number_range = range(Constants.BOARD_SIZE)

        self.grid = [[Position((column, row)) for row in number_range]
                     for column in number_range]

    def player_view(self, player):

        print("{}'s - Board".format(player.name))

        view = Constants.BOARD_HEADER + '\n'
        row_num = 1

        for row in self.grid:

            view += str(row_num).rjust(2) + " " + (
                " ".join([location.status for location in row])
            ) + '\n'

            row_num += 1

        print(view)

    def opponent_view(self, player):

        print("{}'s - Board".format(player.name))

        view = Constants.BOARD_HEADER + '\n'
        row_num = 1

        for row in self.grid:

            view += str(row_num).rjust(2) + " " + (
                " ".join([location.status
                          if location.status
                          not in [Constants.VERTICAL_SHIP,
                                  Constants.HORIZONTAL_SHIP]
                          else Constants.EMPTY
                          for location
                          in row])
            ) + '\n'

            row_num += 1

        print(view)

    def print_boards(player, opponent):

        opponent.board.opponent_view(opponent)
        player.board.player_view(player)
        Handler.print_legend()

    def print_final_boards(player1, player2):

        player1.board.player_view(player1)
        player2.board.player_view(player2)
        Handler.print_legend()

    def place_ship(**kwargs):

        """
        Puts a ship on starting on the desired coord
        and direction. Returns True is everything is ok
        False if ship overlaps with
        existing ships
        """

        player = kwargs['player']
        row, column = kwargs['coord']
        ship_name, ship_size = kwargs['ship']
        direction = kwargs['direction']

        # This creates a reference to the object, not a copy of it
        grid = player.board.grid

        coords = Position.get_coords(**kwargs)
        enough_space = Position.validate_if_empty(player, coords)

        if enough_space:

            ship = Ship(**{
                'name': ship_name,
                'size': ship_size,
                'coords': coords,
                'direction': direction
            })

            # Get's the mark to display at that position based on
            # the direction of the ship
            ship_status = (Constants.HORIZONTAL_SHIP if direction == 'h'
                           else Constants.VERTICAL_SHIP)

            # Assining the data to the cell in the board
            for row, column in coords:
                cell = grid[row][column]
                cell.ship = ship
                cell.status = ship_status

            # Adds the ship to the player
            player.ships.append(ship)

            return True

        else:
            print("Error: Ships overlap")
            return False
