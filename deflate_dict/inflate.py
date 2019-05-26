from typing import Dict
from .is_leaf import is_leaf
from .dict_to_list import dict_to_list
from .utils import has_numeric_keys

def _to_int(value):
    try:
        return int(value)
    except ValueError:
        return value

def restore_lists(my_dict:Dict)->Dict:
    restored = {
        _to_int(k):v if is_leaf(v) else restore_lists(v) for k,v in my_dict.items()
    }
    
    return dict_to_list(restored) if has_numeric_keys(restored) else restored

def inflate(my_dict:Dict, sep="_")->Dict:
    """Return inflated Dict."""
    items = dict()
    for k, v in my_dict.items():
        keys = k.split(sep)
        sub_items = items
        for ki in keys[:-1]:
            try:
                sub_items = sub_items[ki]
            except KeyError:
                sub_items[ki] = dict()
                sub_items = sub_items[ki]
            
        sub_items[keys[-1]] = v

    return restore_lists(items)