from typing import Dict

def has_numeric_keys(my_dict:Dict)->bool:
    """Return boolean representing if given dict has both numeric keys and in continous range.
        my_dict:Dict, dictionary to validate property of.
    """
    keys = set(my_dict.keys())
    return all(
        isinstance(k, int) for k in keys
    ) and min(keys)==0 and max(keys) == len(keys)-1 and keys == set(range(max(keys)+1))