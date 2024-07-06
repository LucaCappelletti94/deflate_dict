"""Test illegal inputs."""

import pytest
from deflate_dict import deflate, inflate
from deflate_dict.utils import type_encode, type_decode

def test_illegal():
    """Test illegal inputs."""
    with pytest.raises(AssertionError):
        deflate(())

    with pytest.raises(AssertionError):
        inflate(())

    with pytest.raises(NotImplementedError):
        type_encode(NotImplementedError("AH!"))
    
    with pytest.raises(AssertionError):
        type_decode("jfhg76slhqjdo78")

    with pytest.raises(AssertionError):
        type_decode(())

    with pytest.raises(AssertionError):
        type_decode("()")
    
    with pytest.raises(AssertionError):
        type_decode("")

    with pytest.raises(AssertionError):
        type_decode("str(")
    
    with pytest.raises(AssertionError):
        type_decode("str)")

    with pytest.raises(AssertionError):
        type_decode("listIndexonixi()")

    with pytest.raises(NotImplementedError):
        type_decode("listIndexonixi(HALLO)")
