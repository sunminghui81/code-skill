



DIRECTIONS = ('N', 'E', 'S', 'W')


class Direction(object):
    def __init__(self):
        self._dir = 0

    @property
    def direction(self):
        return DIRECTIONS[self._dir]

    @direction.setter
    def direction(self, d):
        self._dir = DIRECTIONS.index(d)

    def revolving(self, x):
        self._dir = (4 + self._dir + x) % 4
