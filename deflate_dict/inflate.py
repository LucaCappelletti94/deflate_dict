"""Inflate a dictionary."""

from typing import Dict, Union, List
from deflate_dict.is_leaf import is_leaf
from deflate_dict.utils import type_decode, is_encoded_list, decode_list


def restore_lists(my_dict: Dict, leave_tuples: bool) -> Union[Dict, List]:
    """Restore lists from dictionary.

    Parameters
    ----------
    my_dict : dict
        Dictionary to restore lists from.
    leave_tuples : bool
        Leave tuples as they are.
    """
    restored: Dict = {
        k: (
            v
            if is_leaf(v) or leave_tuples and isinstance(v, tuple)
            else restore_lists(v, leave_tuples)
        )
        for k, v in my_dict.items()
    }

    return decode_list(restored) if is_encoded_list(restored) else restored


def inflate(
    my_dict: Dict, sep="_", leave_tuples=False, type_decode_key: bool = True
) -> Union[List, Dict]:
    """Return inflated Dict.

    Parameters
    ----------
    my_dict : dict
        Dictionary to inflate.
    sep : str, optional
        Separator to use for keys, by default "_"
    leave_tuples : bool, optional
        Leave tuples as they are, by default False
    type_decode_key : bool, optional
        Decode keys from types, by default True

    Raises
    ------
    AssertionError
        If input is not a dictionary.
    """
    assert isinstance(
        my_dict, dict
    ), f"Input must be a dictionary, not {type(my_dict)}!"
    items: Dict = {}
    for key, value in my_dict.items():
        keys = key.split(sep)
        sub_items = items
        for sub_key in keys[:-1]:
            sub_key = type_decode(sub_key) if type_decode_key else sub_key
            try:
                sub_items = sub_items[sub_key]
            except KeyError:
                sub_items[sub_key] = {}
                sub_items = sub_items[sub_key]

        sub_items[type_decode(keys[-1]) if type_decode_key else keys[-1]] = value
    return restore_lists(items, leave_tuples=leave_tuples)
