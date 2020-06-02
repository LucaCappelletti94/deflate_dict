from typing import Dict
from .is_leaf import is_leaf
import sys
import re
from .utils import type_decode, is_encoded_list, decode_list


def restore_lists(my_dict: Dict, leave_tuples:bool)->Dict:
    restored = {
        k: v if is_leaf(v) or leave_tuples and isinstance(v, tuple) else restore_lists(v, leave_tuples)
        for k, v in my_dict.items()
    }

    return decode_list(restored) if is_encoded_list(restored) else restored

def inflate(my_dict: Dict, sep="_", leave_tuples=False, type_decode_key: bool = True)->Dict:
    """Return inflated Dict."""
    items = dict()
    for k, v in my_dict.items():
        keys = k.split(sep)
        sub_items = items
        for ki in keys[:-1]:
            ki = type_decode(ki) if type_decode_key else ki
            try:
                sub_items = sub_items[ki]
            except KeyError:
                sub_items[ki] = dict()
                sub_items = sub_items[ki]

        sub_items[type_decode(keys[-1]) if type_decode_key else keys[-1]] = v
    return restore_lists(items, leave_tuples=leave_tuples)
