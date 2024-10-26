"""Utility functions for encoding and decoding lists as dictionary keys."""

from typing import Dict, Any, List


def is_list_index(my_object: Any) -> bool:
    """Return boolean representing whetever given object is a list index.

    Parameters
    ----------
    my_object : any
        Object to identify list index property of.
    """
    return (
        isinstance(my_object, str)
        and my_object.startswith("listIndex(")
        and my_object.endswith(")")
    )


def encode_list(my_list: List) -> Dict:
    """Encode a list as a dictionary.

    Parameters
    ----------
    my_list : list
        List to encode as dictionary.
    """
    return {f"listIndex({key})": value for key, value in enumerate(my_list)}


def is_encoded_list(candidate: Dict) -> bool:
    """Return boolean representing whetever given object is an encoded list.

    Parameters
    ----------
    candidate : list
        Object to identify encoded list property of.
    """
    return all(is_list_index(e) for e in candidate)


def decode_list(my_list: Dict) -> List:
    """Decode a dictionary to a list.

    Parameters
    ----------
    my_list : dict
        Dictionary to decode as list.
    """
    return list(my_list.values())
