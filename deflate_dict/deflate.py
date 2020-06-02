from typing import Dict, Generator
from .is_leaf import is_leaf
from .utils import type_encode, encode_list


def _deflate(my_dict: Dict, sep="_", root="", leave_tuples: bool = False, type_encode_key: bool = True) -> Generator:
    """Return deflated Dict."""
    separator = sep if root else ""
    for key, value in my_dict.items():
        flatten_key = "{root}{separator}{key}".format(
            root=root, separator=separator, key=type_encode(key) if type_encode_key else key)
        if is_leaf(value) or leave_tuples and isinstance(value, tuple):
            yield (flatten_key, value)
        else:
            for sub_key, sub_value in _deflate(encode_list(value) if isinstance(value, list) else value, sep=sep, root=flatten_key, type_encode_key=type_encode_key):
                yield (sub_key, sub_value)


def deflate(my_dict: Dict, sep="_", root="", leave_tuples: bool = False, type_encode_key: bool = True) -> Dict:
    """Return deflated Dict."""
    return dict(_deflate(
        my_dict,
        sep=sep,
        root=root,
        leave_tuples=leave_tuples,
        type_encode_key=type_encode_key
    ))
