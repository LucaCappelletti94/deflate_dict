"""Test list encoding and decoding"""

from deflate_dict import deflate, inflate
from .utils import match


def test_list_encoding():
    """Test list encoding and decoding."""
    my_dict = {"root": [0, 2, {"weight": 67}]}
    assert match(my_dict, inflate(deflate(my_dict)))


def test_non_list_encoding():
    """Test non list encoding and decoding."""
    my_dict = {"root": {0: 0, 1: 2, 2: {"weight": 67}}}
    assert match(my_dict, inflate(deflate(my_dict)))
