"""Module for checking iterability of objects."""

from typing import Any


def is_iterable(candidate: Any) -> bool:
    """Return boolean representing whetever given object is an iterable.
        candidate, object to identify iterability property of.

    Parameters
    ----------
    candidate : any
        Object to identify iterability property of.
    """
    try:
        iter(candidate)
        return True
    except TypeError:
        return False
