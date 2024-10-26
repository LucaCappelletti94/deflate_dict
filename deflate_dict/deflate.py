"""Deflate a dictionary to a flat dictionary."""

from typing import Dict, Generator
from deflate_dict.is_leaf import is_leaf
from deflate_dict.utils import type_encode, encode_list


def _deflate(
    my_dict: Dict,
    sep="_",
    root="",
    leave_tuples: bool = False,
    type_encode_key: bool = True,
) -> Generator:
    """Return deflated Dict.

    Parameters
    ----------
    my_dict : dict
        Dictionary to deflate.
    sep : str, optional
        Separator to use for keys, by default "_"
    root : str, optional
        Root key to use, by default ""
    leave_tuples : bool, optional
        Leave tuples as they are, by default False
    type_encode_key : bool, optional
        Encode keys as types, by default True
    """
    separator = sep if root else ""
    for key, value in my_dict.items():
        flatten_key = f"{root}{separator}{type_encode(key) if type_encode_key else key}"
        if is_leaf(value) or leave_tuples and isinstance(value, tuple):
            yield (flatten_key, value)
        else:
            for sub_key, sub_value in _deflate(
                encode_list(value) if isinstance(value, list) else value,
                sep=sep,
                root=flatten_key,
                leave_tuples=leave_tuples,
                type_encode_key=type_encode_key,
            ):
                yield (sub_key, sub_value)


def deflate(
    my_dict: Dict,
    sep="_",
    root="",
    leave_tuples: bool = False,
    type_encode_key: bool = True,
) -> Dict:
    """Return deflated Dict.

    Parameters
    ----------
    my_dict : dict
        Dictionary to deflate.
    sep : str, optional
        Separator to use for keys, by default "_"
    root : str, optional
        Root key to use, by default ""
    leave_tuples : bool, optional
        Leave tuples as they are, by default False
    type_encode_key : bool, optional
        Encode keys as types, by default True

    Raises
    ------
    AssertionError
        If input is not a dictionary.
    """
    assert isinstance(
        my_dict, dict
    ), f"Input must be a dictionary, not {type(my_dict)}."

    return dict(
        _deflate(
            my_dict,
            sep=sep,
            root=root,
            leave_tuples=leave_tuples,
            type_encode_key=type_encode_key,
        )
    )
