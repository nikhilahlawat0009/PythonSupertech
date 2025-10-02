# ! /usr/bin/env python3     SHEBANG
# Author: Nikhil Ahlawat
# Version: 1.0
# Description:


import unittest


class TestHighestNumberFinder(unittest.TestCase):
    def test_find_highest_in_list_one_result_single_item(self):

        input_value =[10]
        expected_result = 10

        cut = HighestNumberFinder()

        cut.find_highest_number(input_value)

        self.assertEqual(actual_result, expected_result)
