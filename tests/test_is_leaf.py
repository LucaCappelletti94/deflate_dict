"""Test the is_leaf function from the deflate_dict package."""

from deflate_dict.is_leaf import is_leaf


def test_is_leaf():
    """Test is_leaf."""
    assert is_leaf("ghgh")
    assert is_leaf(33)
    assert is_leaf((1, 2))
    assert is_leaf([1, 2])
    assert is_leaf(["dd", "dd"])
    assert not is_leaf({"a": 3})
    assert not is_leaf([{"a": 3}])
    assert not is_leaf(({"a": 3}, {"a": 3}))
