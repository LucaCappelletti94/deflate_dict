def is_iterable(candidate)->bool:
    """Return boolean representing whetever given object is an iterable.
        candidate, object to identify iterability property of.
    """
    try:
        iter(candidate)
        return True
    except TypeError:
        return False