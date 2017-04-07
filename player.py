from constants import Constants
from handler import Handler

from board import Board
from ship import Ship
from position import Position


class Player:

    def __init__(self,message):

        self.board = Board()
        self.ships = []
        self.guesses = []

        while True:

            print(message)
            name = input('>').strip()

            if not name:
                print('Please enter a valid name blank spaces are not allowed')
                input('Press enter to try again')
                Handler.clear_screen()
                continue

            else:
                self.name = name
                break
        

    def set_fleet(self):

        """
        Ask the user to set all the ships in their board

        """

        print('{}. Time to set your fleet'.format(self.name))
        input('Press ENTER to continue')
        Handler.clear_screen()

        for ship_name, ship_size in Constants.SHIP_INFO:

            while True:

                Handler.clear_screen()
                self.board.player_view(self)
                print("Place: '{}', Length: {}".format(ship_name, ship_size))
                print("Where do you want to place your ship?")

                coord = Position.create_coord()

                if not coord:
                    input("Press enter to try again")
                    continue

                row, column = coord

                # Checking if the coord the user entered has already a ship
                if self.board.grid[row][column].ship:
                    print("Error: There's already a ship at that coord")
                    input("Press enter to try again")
                    continue

                # Asking for the ship direction
                while True:

                    Handler.clear_screen()
                    self.board.player_view(self)
                    print("Place: '{}', Length: {}".format(ship_name, ship_size))
                    direction = Position.get_direction()

                    if not direction:
                        input("Press enter to try again")
                        continue
                    else:
                        break


                # If the player wants to put the ship horizontally
                # the changing number in the coord would be the column
                # and viceversa

                axis = column if direction == 'h' else row

                # Very straight forward. We subtract the axis from the
                # board to see if there is enough space to place the ship.
                # Let's say the user wants to put a 5 places lenght ship
                # horizontally  starting on (8,0) and our board is a 10x10 grid,
                # the ship will ocuppy  (8,0)(9,0)(10,0),(11,0)(12,0).
                # This is wrong. So we take the axis and substract
                # it to the BOARD_SIZE. In our example is 10 - 8, and then
                # compare it to the ship lenght 10 - 8 < 5 which is False

                if Constants.BOARD_SIZE - axis < ship_size:

                    print("The ship don't fit.")
                    input("Press enter to try again")
                    continue

                else:

                    # If nothing wrong, a dict with the ship is created, to send
                    # it to Board.place_ship where it would be proccessed
                    ship = {
                        'ship': (ship_name, ship_size),
                        'player': self,
                        'coord': (row, column),
                        'direction': direction
                    }

                    # Place ship returns a boolean, more info the function
                    if Board.place_ship(**ship):
                        break
                    else:
                        input('Press enter to try again continue')
                        continue

        Handler.clear_screen()
        self.board.player_view(self)
        print('Nice {}. This is your board'.format(self.name))
        input('Press ENTER to continue')

    def has_live_ships(self):
        """Check if the user still have ships"""

        response = False

        for ship in self.ships:
            if not ship.sunk:
                response = True
                break  # Breaking the loop so it will be faster

        return response

    def turn(self, opponent):

        """ 
        This functions let's the user take a turn to guess

        Args:
            opponent -> The other player object
        """

        input("{}'s turn. Press enter to continue".format(self.name))

        while True:

            Handler.clear_screen()
            Board.print_boards(self, opponent)
            print("{}, where do you want to shot at?".format(self.name))

            coord = Position.create_coord()

            # This will be invalid if something is wrong with the coord entered
            # more info in the function
            if not coord:
                input('Press enter to try again')
                continue

            # Check if the user already wrote that coord
            if coord in self.guesses:
                print('Ops! You already tried that coord')
                input('Press enter to try again')
                continue
        
            row, column = coord

            # Creating a reference to the opponents board cell for ease of use
            cell = opponent.board.grid[row][column]

            # Checking if the guess coord is actually an opponent's ship coord
            if cell.ship:

                # Ship.hit returns a boolean telling if the ship have sunk
                sunk = cell.ship.hit(coord)

                if sunk:

                    # Loop through each coord of the ship to change the status of 
                    # the cells to SUNK
                    for row, column in cell.ship.coords:
                        opponent.board.grid[row][column].status = Constants.SUNK

                    Handler.clear_screen()
                    Board.print_boards(self, opponent)
                    print("OMG {}. You sunk one of {}'s ships!".format(self.name,opponent.name))
                    
                else:

                    # If ship not sunk yet, adding a hit only at this position
                    cell.status = Constants.HIT
                    Handler.clear_screen()
                    Board.print_boards(self, opponent)
                    print("Outstanding {}. You hitted!".format(self.name))
                

            else:

                cell.status = Constants.MISS

                Handler.clear_screen()
                Board.print_boards(self, opponent)            
                print("Ops {}, you've missed".format(self.name))

            # Saving the coord in the player guesses for furter comparisons
            self.guesses.append(coord)

            input('Press enter to continue')
            Handler.clear_screen()

            break
