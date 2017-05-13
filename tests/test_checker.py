import unittest

from flake8_sorted_keys import SortedKeysChecker


class SortedKeysCheckerTestCase(unittest.TestCase):

    def test_checker_implements_interface(self):
        getattr(SortedKeysChecker, 'run')

    def test_unsorted_keys(self):
        pass


class SortedKeysCheckerNegativeTestCase(unittest.TestCase):

    def test_single_line_dict(self):
        pass

    def test_numeric_keys(self):
        pass

    def test_embedded_unpacking(self):
        pass
