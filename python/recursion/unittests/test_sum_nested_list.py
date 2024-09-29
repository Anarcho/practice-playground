from sum_nested_lists.sum_nested_lists import sum_nested_lists
import sys
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__)))


class TestSumNestedList(unittest.TestCase):
    def run_test_case(self, test_input, expected_output):
        print(f"Input: {test_input}")
        print(f"Expected Output: {expected_output}")
        actual_output = sum_nested_list(test_input)
        print(f"Actual Output: {actual_output}")
        try:
            self.assertEqual(actual_output, expected_output)
            print("Test Result: PASS")
        except AssertionError:
            print("Test Result: FAIL")
        print("------------------------")

    def test_simple_flat_list(self):
        self.run_test_case([1, 2, 3, 4, 5], 15)

    def test_nested_list_with_one_level(self):
        self.run_test_case([1, [2, 3], 4, [5, 6]], 21)

    def test_deeply_nested_list(self):
        self.run_test_case([1, [2, [3, [4, [5]]]]], 15)

    def test_mixed_nested_list(self):
        self.run_test_case([1, [2, 3], [4, [5, 6]], 7, [8, [9, 10]]], 55)

    def test_empty_and_nested_empty_lists(self):
        self.run_test_case([[], [[], []], [], [[[]]]], 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
