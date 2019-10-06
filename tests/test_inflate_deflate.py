from deflate_dict import inflate, deflate
from .utils import test_dict
from random_dict import random_int_dict, random_float_dict
from tqdm.auto import tqdm


def test_inflate_deflate():
    dictionaries = [test_dict] + [
        random_int_dict(4, 4) for i in range(100)
    ] + [
        random_float_dict(4, 4) for i in range(100)
    ]
    for d in tqdm(dictionaries):
        assert d == inflate(deflate(d))
