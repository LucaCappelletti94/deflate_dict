from deflate_dict import deflate, inflate

def test_tuple_keys():
    my_dict = {
        (1,"d"):6,
        (56, 56,"d"):6,
        (1,"d", True):6
    }
    assert my_dict == inflate(deflate(my_dict))