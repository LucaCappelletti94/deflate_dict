"""Test illegal inputs."""

import pytest
from deflate_dict import deflate, inflate


def test_illegal():
    """Test illegal inputs."""
    with pytest.raises(AssertionError):
        deflate(())

    with pytest.raises(AssertionError):
        inflate(())
