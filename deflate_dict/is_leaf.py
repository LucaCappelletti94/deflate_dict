"""Module for determining if given node is a leaf."""

from typing import Any
from deflate_dict.utils import is_iterable


def is_leaf(node: Any) -> bool:
    """Returns whether given node is a leaf.

    Parameters
    ----------
    node : any
        Element to determine if is leaf.

    Implementative details
    ----------------------
    A leaf is not iterable or a dict with no iterable elements.
    """
    return (
        not is_iterable(node)
        or not isinstance(node, dict)
        and not any(isinstance(e, (list, dict)) for e in node)
    )
