
from robot.position import Position
from robot.cmd import Cmd


class Robot(Cmd):
    def __init__(self):
        super(Robot, self).__init__()
        self.position = Position()

    def do(self):
        for cmd in self.cmds:
            self.action(cmd, self.position)
