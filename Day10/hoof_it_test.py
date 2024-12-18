import unittest

from Day10.hoof_it import create_map, find_trail_head, find_next_step, find_trail, find_array_bounds


class testHoofIt(unittest.TestCase):
    def test_find_trail_head(self):
        input = [[1,1,1],[1,0,1],[1,1,1]]
        expected = [1,1]

        actual = find_trail_head(input)

        self.assertEqual(expected, actual)

    def test_create_map(self):
        input = """111
101
111"""

        expected = [[1,1,1],[1,0,1],[1,1,1]]

        actual = create_map(input)

        self.assertEqual(expected, actual)

    def test_find_next_step(self):
        map = [[2,2,2],[2,0,1],[2,2,2]]
        start_point = [1,1]

        expected = [1,2]

        actual = find_next_step(map, start_point)

        self.assertEqual(expected, actual)

        map = [[2, 1, 2], [2, 0, 2], [2, 2, 2]]
        start_point = [1, 1]

        expected = [0, 1]

        actual = find_next_step(map, start_point)

        self.assertEqual(expected, actual)

        map = [[2, 2, 2], [1, 0, 2], [2, 2, 2]]
        start_point = [1, 1]

        expected = [1, 0]

        actual = find_next_step(map, start_point)

        self.assertEqual(expected, actual)

        map = [[2, 2, 2], [1, 0, 2], [2, 2, 2]]
        start_point = [1, 1]

        expected = [1, 0]

        actual = find_next_step(map, start_point)

        self.assertEqual(expected, actual)

        map = [[2, 0, 2], [2, 1, 2], [2, 2, 2]]
        start_point = [0, 1]

        expected = [1, 1]

        actual = find_next_step(map, start_point)

        self.assertEqual(expected, actual)

        map = [[2, 2, 2], [0, 2, 2], [1, 2, 2]]
        start_point = [1, 0]

        expected = [2, 0]

        actual = find_next_step(map, start_point)

        self.assertEqual(expected, actual)

    def test_find_array_bounds(self):
        input = [[2, 2, 2], [0, 2, 2], [1, 2, 2]]
        expected = [3, 3]

        actual = find_array_bounds(input)

        self.assertEqual(expected, actual)


    def test_take_two_steps(self):
        map = [[3,3,2],[2,0,1],[2,2,3]]
        starting_point = [1, 1]
        target_number = 3

        expected = [0, 2]

        actual = find_trail(map, starting_point, target_number, [3, 3])

        self.assertEqual(expected, actual)

        map = [[0,1,2,3],[1,2,3,4],[8,7,6,5],[9,8,7,6]]
        starting_point = [0, 0]
        target_number = 9

        expected = [4, 0]

        actual = find_trail(map, starting_point, target_number, [4, 4])

        self.assertEqual(expected,actual)

if __name__ == '__main__':
    unittest.main()