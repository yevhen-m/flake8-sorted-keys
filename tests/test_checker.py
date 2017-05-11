import unittest

from flake8_sorted_keys import SortedKeysChecker


class SortedKeysCheckerTestCase(unittest.TestCase):

    def test_checker_implements_interface(self):
        getattr(SortedKeysChecker, 'run')
