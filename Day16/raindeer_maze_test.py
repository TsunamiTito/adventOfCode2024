import unittest

from Day16.map import Maze
from Day16.raindeer import Raindeer

class TestRaindeerMaze(unittest.TestCase):

    def test_create_raindeer(self):
        expected_x = 3
        expected_y = 5

        new_raindeer = Raindeer(expected_x, expected_y)

        self.assertEqual(expected_x, new_raindeer.x_position)
        self.assertEqual(expected_y, new_raindeer.y_position)

    def test_raindeer_move(self):
        expected_ending_x = 3
        expected_ending_y = 4

        the_raindeer = Raindeer(3, 5)

        the_raindeer.take_a_step()

        self.assertEqual(expected_ending_x, the_raindeer.x_position)
        self.assertEqual(expected_ending_y, the_raindeer.y_position)

    def test_creating_new_map(self):
        input = """###
###
###"""

        print(Maze(input).maze)


if __name__ == '__main__':
    unittest.main()