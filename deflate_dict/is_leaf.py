from .utils import is_iterable

def is_leaf(node)->bool:
    """Return boolean representing whetever given node is a leaf: does not contain lists or dictionaries.
        node, the element to determine if is leaf.
    """
    return not is_iterable(node) or not isinstance(node, dict) and not any([
        isinstance(e, (list, dict)) for e in node
    ])