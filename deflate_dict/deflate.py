from typing import Dict, Generator
from .is_leaf import is_leaf
from .list_to_dict import list_to_dict

def _deflate(my_dict:Dict, sep="_", root="")->Generator:
    """Return deflated Dict."""
    for key, value in my_dict.items():
        flatten_key = "{root}{sep}{key}".format(root=root, sep=sep if root else "", key=key)
        if is_leaf(value):
            yield (flatten_key, value)
        else:    
            for sub_key, sub_value in _deflate(list_to_dict(value) if isinstance(value, list) else value, sep=sep, root=flatten_key):
                yield (sub_key, sub_value)

def deflate(my_dict:Dict, sep="_", root="")->Dict:
    """Return deflated Dict."""
    return dict(_deflate(my_dict, sep=sep, root=root))