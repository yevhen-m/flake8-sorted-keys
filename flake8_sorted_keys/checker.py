__version__ = '0.1.0'

import ast


class SortedKeysChecker(object):
    name = 'flake8-sorted-keys'
    version = __version__

    message = "S001 Sort keys. '{0}' should be before '{1}'."

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
                for key1, key2 in zip(node.keys, node.keys[1:]):
                    if key2.s < key1.s:
                        yield (
                            key2.lineno,
                            key2.col_offset,
                            self.message.format(key2.s, key1.s),
                            type(self),
                        )
