

from robot.direction import Direction

class Position(Direction):
    def __init__(self):
        super(Position, self).__init__()
        self.x = 0
        self.y = 0
        self.x_min = -6
        self.x_max = 6
        self.y_min = -6
        self.y_max = 6

    @property
    def value(self):
        return self.x, self.y, self.direction

    def moving(self, step):
        if self.direction == 'N':
            self.y += step
        if self.direction == 'E':
            self.x += step
        if self.direction == 'W':
            self.x -= step
        if self.direction == 'S':
            self.y -= step

    def is_in(self):
        if not self.x in range(self.x_min, self.x_max):
            return False
        if not self.y in range(self.y_min, self.y_max):
            return False
        return True

    def try_move(self, direction):
        target = Position()
        target.x = self.x
        target.y = self.y
        target.direction = self.direction
        print(target.value)
        target.moving(direction)
        return target if target.is_in() else None