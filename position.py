from constants import Constants


class Position:

    def __init__(self, coord):

        self.coord = coord
        self.ship = None
        self.status = Constants.EMPTY

    def __str__(self):

        position_info = {
            'coord': self.coord,
            'ship': self.ship,
            'status': self.status
        }

        return '{coord} {ship} {status}'.format(**position_info)

    def create_coord():

        """
        Ask the user for a coord. Verifies its valid

        Returns:
            Tuple with two integer values
        """
        response = True

        # Get the input and upper it to ensure the letter is uppercased
        coord = input('Example "A1": >').upper().strip()

        if not coord:
            print('Error: Blank spaces are not allowed')
            response = False

        # Handling the coord is only one character length, e.g 'a'
        elif len(coord) < 2:
            print('Error: Your coord is to small')
            response = False

        else:

            # Converting this to a number
            # Ord gets the unicode for a character string they are seriated, so
            # ord('A') - ord('A') = 0 and ord('B') - ord('A') = 1 and so on
            # by getting the difference between them i obtain the column
            # of the board

            if not coord[0].isalpha():
                print('Error: First part of the coord should be a letter')
                column = None
                response = False
            else:
                column = ord(coord[0]) - ord('A')

            # Take one from the val because the array starts in 0
            # so if the user wants to put in A1, the coord
            # will become (0,0)

            try:
                row = int(coord[1:])
            except ValueError:
                print('Error: Second part of the coord should be a '
                      'whole number')
                row = None
                response = False
            else:
                row -= 1

            if row is not None and column is not None:
                # Check if the coords don't exists in the table
                if (Constants.BOARD_SIZE - row < 0 or
                        Constants.BOARD_SIZE - column < 0):
                    print("Error: Your coord doesn't exist in the board")
                    response = False

            # Returning a false if something is wrong, else return the coord
            return response if response is False else (row, column)

    def get_coords(**kwargs):

        """
        Returns a list with the coords starting at the
        one the user entered, plus the ship size at
        the direction the user prompted

        Args:
            coord : Tuple (row, column) Where the user want's to put the ship
            ship : Tuple with ship name and size
            direction : Either 'v' or 'h', standing for vertical and horizontal
        """

        coords = []

        row, column = kwargs['coord']
        ship_name, ship_size = kwargs['ship']
        direction = kwargs['direction']

        if direction == 'h':

            # If the direction is horizontal, what should be incresed
            # is the column. Example:
            # Coord is (row,column)
            # Let's say we will start at (0,1)
            # Then in the grid it should be:
            # (0,1)(0,2)(0,3) etc

            for position in range(ship_size):
                coords.append((row, column))
                column += 1

        elif direction == 'v':

            # The opposite case, here what it's increased is the row
            # (1,0)(2,0)(3,0)

            for position in range(ship_size):

                coords.append((row, column))
                row += 1

        return coords

    def validate_if_empty(player, coords):

        """
        Validates if the coords where the user
        wants to put the ship are free or they overlap
        with another ship
        """

        response = True

        for row, column in coords:

            if player.board.grid[row][column].ship:
                response = False

        return response

    def get_direction():

        """
        Ask the user to prompt the direction in which
        the ship should be placed

        Returns eiter the direction if its valid or False
        """
        message = 'Place ship [V]ertical or [H]orizontal: '
        direction = input(message).lower().strip()

        if direction == 'v' or direction == 'h':
            return direction
        elif not direction:
            print('Error: Blank spaces are not allowed')
        else:
            print('Enter a valid ship direction')

        return False
