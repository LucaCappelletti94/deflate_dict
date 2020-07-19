import pytest
from deflate_dict import deflate, inflate


def test_illegal():
    with pytest.raises(ValueError):
        deflate(())

    with pytest.raises(ValueError):
        inflate(())
