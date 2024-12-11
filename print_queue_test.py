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
        expected: page = page(47,53)

        actual:page = create_page(input,[])

        self.assertTrue(assert_two_pages(expected,actual))


    def test_create_one_line(self):
        input = """47|53
97|13"""
        expected = [page(47,53),page(97,13)]

        actual: List[page] = create_page_rules(input)

        self.assertTrue(assert_two_pages(expected[0],actual[0]))
        self.assertTrue(assert_two_pages(expected[1],actual[1]))

        input = """47|53
97|13
97|61"""
        expected = [page(47,53),page(97,[13,61])]

        actual: List[page] = create_page_rules(input)

        self.assertTrue(assert_two_pages(expected[0], actual[0]))
        self.assertTrue(assert_two_pages(expected[1], actual[1]))


if __name__ == '__main__':
    unittest.main()