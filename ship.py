class Ship:

    def __init__(self, **kwargs):

        self.name = kwargs['name']
        self.size = kwargs['size']
        self.coords = kwargs['coords']
        self.direction = kwargs['direction']
        self.sunk = False
        self.hits = []

    def __str__(self):

        ship = {
            'name': self.name,
            'size': self.size,
            'coords': self.coords,
            'direction': self.direction,
            'sunk': self.sunk
        }

        return "{name}, Size: {size}, {coords}, {direction}".format(**ship)

    def hit(self, coord):

        """
        Takes a hit on the ship and returns a boolean
        with True if the ship has sunked and False if not
        """
        sunk = False

        self.hits.append(coord)

        if len(self.hits) == self.size:
            sunk = True
            self.sunk = sunk

        return sunk
