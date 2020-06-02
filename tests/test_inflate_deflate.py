from deflate_dict import inflate, deflate
from .utils import test_dict
from random_dict import random_int_dict, random_float_dict, random_string_dict


def test_inflate_deflate():
    dictionaries = [test_dict] + [
        random_int_dict(4, 4) for i in range(100)
    ] + [
        random_float_dict(4, 4) for i in range(100)
    ] + [
        random_string_dict(4, 4) for i in range(100)
    ]
    for d in dictionaries:
        assert d == inflate(deflate(d))
        assert d == inflate(deflate(d, leave_tuples=True), leave_tuples=True)

    string_dictionaries = [
        {"test": {"test": {"test": [1, 2, 3, 4]}}}
    ]
    for d in string_dictionaries:
        assert d == inflate(
            deflate(d, type_encode_key=False), type_decode_key=False)
        assert d == inflate(
            deflate(d, leave_tuples=True, type_encode_key=False), leave_tuples=True, type_decode_key=False)
