#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_max_at_end(self):
        """Test with max at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test with max at the beginning"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test with max in the middle"""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_one_negative_number(self):
        """Test with one negative number in the list"""
        self.assertEqual(max_integer([1, 2, -5, 3]), 3)

    def test_only_negative_numbers(self):
        """Test with only negative numbers in the list"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_list_one_element(self):
        """Test with list of one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_list_empty(self):
        """Test with empty list"""
        self.assertEqual(max_integer([]), None)

    def test_unordered_list(self):
        """Test with unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        """Test with single element list"""
        self.assertEqual(max_integer([42]), 42)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-10, -5, -20]), -5)

    def test_mixed_positive_negative(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-5, 0, 5, 10]), 10)

    def test_duplicates(self):
        """Test with duplicate maximum values"""
        self.assertEqual(max_integer([1, 4, 4, 3]), 4)

    def test_all_same(self):
        """Test with all same values"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_two_elements(self):
        """Test with two elements"""
        self.assertEqual(max_integer([1, 2]), 2)

    def test_two_elements_reversed(self):
        """Test with two elements in reverse order"""
        self.assertEqual(max_integer([2, 1]), 2)

    def test_default_empty_list(self):
        """Test with default empty list parameter"""
        self.assertEqual(max_integer(), None)

    def test_large_numbers(self):
        """Test with large numbers"""
        self.assertEqual(max_integer([1000000, 999999, 1000001]), 1000001)

    def test_zero_in_list(self):
        """Test with zero in list"""
        self.assertEqual(max_integer([0, -1, -2]), 0)

    def test_single_negative(self):
        """Test with single negative number"""
        self.assertEqual(max_integer([-10]), -10)
