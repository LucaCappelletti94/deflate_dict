from deflate_dict import deflate, inflate
from .utils import match

def test_list_encoding():
    my_dict = {
        "root": [
            0, 2, {
                "weigh":67
            }
        ]
    }
    assert match(my_dict, inflate(deflate(my_dict)))


def test_non_list_encoding():
    my_dict = {
        "root": {
            0: 0,
            1: 2,
            2: {
                "weigh":67
            }
        }
    }
    assert match(my_dict, inflate(deflate(my_dict)))