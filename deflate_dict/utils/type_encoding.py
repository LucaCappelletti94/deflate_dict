"""Encode and decode objects to and from strings."""

from typing import Any
import re
from deflate_dict.utils.list_encoding import is_list_index


def type_encode(my_object: Any) -> str:
    """Encode an object to a string.

    Parameters
    ----------
    my_object : any
        Object to encode as string.
    """
    if is_list_index(my_object):
        return my_object
    classname = my_object.__class__.__name__
    if classname in ("bool", "int", "float", "str"):
        return f"{classname}({my_object})"
    if classname == "tuple":
        my_object = ",".join([type_encode(e) for e in my_object])
        return f"{classname}({my_object})"
    raise NotImplementedError(f"Unable to encode object of type {classname}!")


def type_decode(my_object: str) -> Any:
    """Decode an object from a string.

    Parameters
    ----------
    my_object : str
        Object to decode from string.
    """
    assert isinstance(my_object, str), "Input must be a string!"
    assert "(" in my_object, "Invalid input, missing parentheses!"
    assert ")" in my_object, "Invalid input, missing parentheses!"
    assert len(my_object) > 2, "Invalid input, empty string!"

    pattern = re.compile(r"^(\w+)\((.+)\)$")
    results = pattern.findall(my_object)
    if not results:
        if my_object == "str()":
            # This happens only in the case of empty string "" being coded as str().
            return ""
        raise AssertionError(f"Invalid empty string input: {my_object}")
    object_class, value = results[0]
    if object_class == "str":
        return value
    if object_class == "bool":
        return bool(value)
    if object_class == "int":
        return int(value)
    if object_class == "float":
        return float(value)
    if object_class == "tuple":
        return tuple(type_decode(val) for val in value.split(","))
    if object_class in "listIndex":
        return my_object
    raise NotImplementedError(f"Class {object_class} is not currently supported!")
