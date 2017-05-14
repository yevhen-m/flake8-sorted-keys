import ast
import unittest

from flake8_sorted_keys import SortedKeysChecker


class SortedKeysCheckerBaseTestCase(unittest.TestCase):

    def check_snippet(self, code_snippet, filename='__main__'):
        tree = ast.parse(code_snippet)
        checker = SortedKeysChecker(tree, filename)
        return list(checker.run())


class SortedKeysCheckerPositiveBaseTestCase(SortedKeysCheckerBaseTestCase):

    def test_unsorted_keys(self):
        code = '''dict_literal = {
                    'a': 'a',
                    'c': 'c',
                    'b': 'b',
                  }'''
        lint_errors = self.check_snippet(code)
        for error in lint_errors:
            offset, line, msg, _ = error
            self.assertIn('S001', msg)


class SortedKeysCheckerNegativeBaseTestCase(SortedKeysCheckerBaseTestCase):

    def test_single_line_dict(self):
        code = '''dict_literal = {'a': 'a', 'c':'c', 'b': 'b'}'''
        lint_errors = self.check_snippet(code)

        self.assertFalse(lint_errors)

    def test_numeric_keys(self):
        code = '''dict_literal = {'1': 'a', '3':'c', '2': 'b'}'''
        lint_errors = self.check_snippet(code)

        self.assertFalse(lint_errors)
