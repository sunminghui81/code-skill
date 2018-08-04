


class _Command(object):
    def __init__(self, rd=0, rt=0, md=0, mt=0):
        self.revolving_direction = rd
        self.revolving_times = rt
        self.moving_direction = md
        self.moving_times = mt

    def move_times(self, n):
        if n in range(0, 10):
            self.moving_times = n
            return self
        else:
            raise ValueError('step [0, 10]')

    def repeat(self, n):
        if n in range(1, 10):
            return [self] * (n + 1)
        else:
            raise ValueError('repeat [1, 10]')

LEFT = _Command(-1, 1, 0, 0)
RIGHT = _Command(1, 1, 0, 0)
ROUND = _Command(1, 2, 0, 0)
FORWORD = _Command(0, 0, 1, 1)
BACKWORD = _Command(0, 0, -1, 1)
FORWORDN = lambda n: _Command(0, 0, 1, 1).move_times(n)
BACKWORDN = lambda n: _Command(0, 0, -1, 1).move_times(n)
REPEAT = lambda c, n: c.repeat(n)


class Cmd(object):
    def __init__(self):
        super(Cmd, self).__init__()
        self.cmds = []

    def insert_cmd(self, *args):
        for cmd in args:
            self._insert_cmd(cmd)

    def _insert_cmd(self, cmd):
        try:
            isinstance(cmd, type(_Command))
            self.cmds.append(cmd)
        except Exception as e:
            raise e

    def safe_mode(self, position):
        while True:
            self.action(LEFT, position)
            if self.action(FORWORD, position):
                return

    def action(self, cmd, position):
        for _ in range(cmd.revolving_times):
            position.revolving(cmd.revolving_direction)
        for _ in range(cmd.moving_times):
            p = position.try_move(cmd.moving_direction)
            if not p:
                self.safe_mode(position)
                return False
            position.x = p.x
            position.y = p.y
        return True

