import unittest
from operator import truediv
from typing import List

from print_queue import page, create_page, create_page_rules


def assert_two_pages(page1:page , page2:page):
    if page1.page_rule == page2.page_rule and page1.page_number == page2.page_number:
        return True
    return False

class TestPrintQueue(unittest.TestCase):
    def test_create_new_page(self):
        input = "47|53"
        expected = [{'47': '53'}]

        actual = create_page(input,[])

        self.assertEqual(expected, actual)


    def test_create_one_line(self):
        input = """47|53
97|13"""
        expected = {'47': ['53'], '97': ['13']}

        actual: List[page] = create_page_rules(input)

        self.assertEqual(expected, actual)

        input = """47|53
97|13
97|61"""
        expected = {'47': ['53'], '97': ['13', '61']}

        actual: List[page] = create_page_rules(input)

        self.assertEqual(expected, actual)

        input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13"""

        expected = {'29': ['13'], '47': ['53', '13', '61', '29'], '53': ['29', '13'], '61': ['13', '53', '29'], '75': ['29', '53', '47', '61', '13'], '97': ['13', '61', '47', '29', '53', '75']}

        actual: List[page] = create_page_rules(input)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()