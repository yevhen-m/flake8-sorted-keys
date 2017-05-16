import ast
import sys
import unittest

from flake8_sorted_keys import SortedKeysChecker


ver_maj, ver_min = sys.version_info.major, sys.version_info.minor


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

        self.assertEqual(len(lint_errors), 1)
        first_error = lint_errors[0]
        line, offset, msg, _ = first_error
        self.assertIn('S001', msg)

    def test_unsorted_keys_embedded_dicts(self):
        code = '''dict_literal = {   # 1  <--
                    'a': 'a',        # 2
                    'c': 'c',        # 3
                    'd': {           # 4  <--
                        'd': 'd',    # 5
                        'f': 'f',    # 6
                        'b': 'b',    # 7
                    },               # 8
                    'b': 'b',        # 9
                  }'''
        lint_errors = self.check_snippet(code)

        self.assertEqual(len(lint_errors), 2)
        first_error, second_error = lint_errors

        line, offset, msg, _ = first_error
        self.assertIn('S001', msg)
        self.assertEqual(line, 1)

        line, offset, msg, _ = second_error
        self.assertIn('S001', msg)
        self.assertEqual(line, 4)


class SortedKeysCheckerNegativeBaseTestCase(SortedKeysCheckerBaseTestCase):

    def test_single_line_dict(self):
        code = '''dict_literal = {'a': 'a', 'c':'c', 'b': 'b'}'''
        lint_errors = self.check_snippet(code)

        self.assertFalse(lint_errors)

    def test_numeric_keys(self):
        code = '''dict_literal = {'1': 'a', '3':'c', '2': 'b'}'''
        lint_errors = self.check_snippet(code)

        self.assertFalse(lint_errors)

    @unittest.skipIf(sys.version_info < (3, 5), 'Need higher python version')
    def test_embedded_unpacking(self):
        code = '''dict_literal = {
                    'a': 'a',
                    'c': 'c',
                    **some_dict,
                    'b': 'b',
                  }'''
        lint_errors = self.check_snippet(code)

        self.assertFalse(lint_errors)
