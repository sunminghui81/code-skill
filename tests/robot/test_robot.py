import  pytest

from robot.robot import Robot
from robot.cmd import *


@pytest.fixture()
def robot():
    return Robot()


class TestRobot(object):

    def test_robot(self, robot):
        assert robot.position.value == (0, 0, 'N')

    def test_left(self, robot):
        robot.insert_cmd(LEFT)
        robot.do()
        assert robot.position.value == (0, 0, 'W')

    def test_forword(self, robot):
        robot.insert_cmd(FORWORD)
        robot.do()
        assert robot.position.value == (0, 1, 'N')

    def test_backword(self, robot):
        robot.insert_cmd(RIGHT)
        robot.insert_cmd(BACKWORD)
        robot.do()
        assert robot.position.value == (-1, 0, 'E')


    def test_round(self, robot):
        robot.insert_cmd(ROUND)
        robot.do()
        assert robot.position.value == (0, 0, 'S')


    def test_forwordn(self, robot):
        robot.insert_cmd(FORWORDN(5))
        robot.do()
        assert robot.position.value == (0, 5, 'N')

    def test_backwordn(self, robot):
        robot.insert_cmd(BACKWORDN(5))
        robot.do()
        assert robot.position.value == (0, -5, 'N')

    def test_forwordn_overrange(self):
        with pytest.raises(ValueError, message='step [0, 10]'):
            FORWORDN(11)

    def test_cmds(self, robot):
        robot.insert_cmd(ROUND, BACKWORDN(5), RIGHT)
        robot.do()
        assert robot.position.value == (0, 5, 'W')

    def test_repeat(self, robot):
        robot.insert_cmd(RIGHT, *REPEAT(FORWORDN(1), 2), LEFT)
        robot.do()
        assert robot.position.value == (3, 0, 'N')

    def test_safe(self, robot):
        robot.insert_cmd(RIGHT, *REPEAT(FORWORDN(4), 1), LEFT)
        robot.do()
        assert robot.position.value == (5, 1, 'W')


