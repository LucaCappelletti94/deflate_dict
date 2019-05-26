from dict_utils import inflate, deflate
from .utils import test_dict

def test_inflate():
    print(inflate(deflate(test_dict)))