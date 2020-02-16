from typing import Dict

def is_list_index(my_object)->bool:
    return isinstance(my_object, str) and my_object.startswith("listIndex(") and my_object.endswith(")")

def encode_list(my_list)->dict:
     return {
        "listIndex({})".format(key):val
        for key, val in enumerate(my_list)
    }

def is_encoded_list(candidate)->bool:
    return all(is_list_index(e) for e in candidate)

def decode_list(my_list:Dict)->dict:
    return list(my_list.values())