class Constants:

    SHIP_INFO = [
        # ("Aircraft Carrier", 5),
        # ("Battleship", 4),
        # ("Submarine", 3),
        # ("Cruiser", 3),
        ("Patrol Boat", 2)
    ]

    BOARD_SIZE = 3
    BOARD_HEADER = "   " + " ".join(
        [chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)])

    VERTICAL_SHIP = '|'
    HORIZONTAL_SHIP = '-'
    EMPTY = 'O'
    MISS = '.'
    HIT = '*'
    SUNK = '#'
