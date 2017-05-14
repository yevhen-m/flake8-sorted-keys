__version__ = '0.0.1'

import ast


class SortedKeysChecker(object):
    name = 'flake8-sorted-keys'
    version = __version__

    unsorted_message = 'S001 Sort keys'

    def __init__(self, tree, *args, **kwargs):
        self.tree = tree

    def needs_checking(self, dict_node):
        """Decide weather specific Dict literal node needs to be considered.

        We are only interested in multi-line dicts with all string keys.
        """
        if not all(isinstance(key, ast.Str) for key in dict_node.keys):
            return False
        line_numbers = [key.lineno for key in dict_node.keys]
        return len(line_numbers) == len(set(line_numbers))

    def run(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Dict) and self.needs_checking(node):
                str_keys = [k.s for k in node.keys]
                if str_keys != sorted(str_keys):
                    yield (
                        node.lineno,
                        node.col_offset,
                        self.unsorted_message,
                        type(self),
                    )
