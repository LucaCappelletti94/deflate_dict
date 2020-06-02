from .is_iterable import is_iterable
import re
from .list_encoding import is_list_index

def type_encode(my_object)->str:
    if is_list_index(my_object):
        return my_object
    classname = my_object.__class__.__name__
    if classname in ("bool", "int", "float", "str"):
        return "{classname}({my_object})".format(
            classname=classname,
            my_object=my_object
        )
    if classname == "tuple":
        return "{classname}({my_object})".format(
            classname=classname,
            my_object=",".join([
                type_encode(e)
                for e in my_object
            ])
        )
    raise ValueError("Unable to encode object of type {classname}!".format(
        classname=classname
    ))

def type_decode(my_object:str):
    pattern = re.compile(r"^(\w+)\((.+)\)$")
    results = pattern.findall(my_object)
    if not results:
        # This happens only in the case of empty string "" being coded as str().
        return ""
    object_class, value = results[0]
    if object_class == "str":
        return value
    if object_class == "bool":
        return bool(value)
    if object_class == "int":
        return int(value)
    if object_class == "float":
        return float(value)
    if object_class == "tuple":
        return tuple([
            type_decode(val)
            for val in value.split(",")
        ])
    if object_class == "listIndex":
        return my_object
    raise ValueError("Class {object_class} is not currently supported!".format(
        object_class=object_class
    ))