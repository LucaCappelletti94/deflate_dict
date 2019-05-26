from deflate_dict import inflate, deflate
from .utils import test_dict

def test_inflate():
    inflate(deflate(test_dict))