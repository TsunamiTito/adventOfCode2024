import unittest
from operator import truediv


from Day7.bridge_repair import read_split_line, is_line_true


class TestBridgeRepair(unittest.TestCase):

    def test_read_split_line(self):
        input = "190: 10 19"

        expected = [190, [10,19]]

        actual = read_split_line(input)

        self.assertEqual(expected,actual)


    def test_line_is_true(self):
        input = [190, [10,19]]

        actual = is_line_true(input)

        self.assertTrue(actual)

    def test_bridge_built_with_addition(self):
        input = [25, [20,5]]

        actual = is_line_true(input)

        self.assertTrue(actual)

    def test_bridge_with_one_step_false(self):
        input = [300, [2,38]]

        actual = is_line_true(input)

        self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()