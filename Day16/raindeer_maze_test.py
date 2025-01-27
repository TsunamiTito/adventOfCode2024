import unittest
from distutils.dep_util import newer

from Day16.map import Maze
from Day16.raindeer import Raindeer

class TestRaindeerMaze(unittest.TestCase):

    def test_create_raindeer(self):
        map = Maze("3x3 map one valid space.txt")
        expected_x = 3
        expected_y = 5

        new_raindeer = Raindeer(expected_x, expected_y, map)

        self.assertEqual(expected_x, new_raindeer.x_position)
        self.assertEqual(expected_y, new_raindeer.y_position)

    def test_raindeer_move(self):
        map = Maze("3x3 map one valid space.txt")
        expected_ending_x = 3
        expected_ending_y = 4

        the_raindeer = Raindeer(3, 5, map)

        the_raindeer.take_a_step()

        self.assertEqual(expected_ending_x, the_raindeer.x_position)
        self.assertEqual(expected_ending_y, the_raindeer.y_position)

    def test_creating_new_map(self):
        input = """###
###
###"""

        expected = [['#', '#', '#'], ['#', '.', '#'], ['#', '#', '#']]
        new_maze = Maze("3x3 map one valid space.txt")

        self.assertEqual(expected, new_maze.maze)

        # big_maze = Maze("day_16_input.txt")

        # big_maze.print_maze()

    def test_map_get_element(self):
        new_maze = Maze("3x3 map one valid space.txt")

        self.assertEqual(".", new_maze.get_element(1,1))
        self.assertEqual("#", new_maze.get_element(0,0))
        self.assertEqual(None, new_maze.get_element(-1,0))
        self.assertEqual(None, new_maze.get_element(4,0))
        self.assertEqual(None, new_maze.get_element(0,-1))
        self.assertEqual(None, new_maze.get_element(0,4))




    def test_take_one_step(self):
        one_step_maze = Maze("one step map.txt")

        randle = Raindeer(1,1, one_step_maze)

        randle.take_a_step()

        self.assertEqual(one_step_maze, randle.raindeer_map)
        self.assertEqual(1, randle.x_position)
        self.assertEqual(2, randle.y_position)

    def test_take_one_step_north(self):
        one_step_maze = Maze("one step north map.txt")

        randle = Raindeer(2,1, one_step_maze)

        randle.take_a_step()

        self.assertEqual(1, randle.x_position)
        self.assertEqual(1, randle.y_position)



if __name__ == '__main__':
    unittest.main()