# 🎈🌵 Deflate Dict

[![pip](https://badge.fury.io/py/deflate-dict.svg)](https://pypi.org/project/deflate-dict/)
[![python](https://img.shields.io/pypi/pyversions/deflate-dict)](https://pypi.org/project/deflate-dict/)
[![license](https://img.shields.io/pypi/l/deflate-dict)](https://pypi.org/project/deflate-dict/)
[![downloads](https://pepy.tech/badge/deflate-dict)](https://pepy.tech/project/deflate-dict)
[![mypy](https://github.com/LucaCappelletti94/deflate_dict/actions/workflows/mypy.yml/badge.svg)](https://github.com/LucaCappelletti94/deflate_dict/actions/)
[![Github Actions](https://github.com/LucaCappelletti94/deflate_dict/actions/workflows/python.yml/badge.svg)](https://github.com/LucaCappelletti94/deflate_dict/actions/)

Python package to deflate 🌵 and re-inflate 🎈 nested dictionaries.

## How do I install this package?

As usual, just download it using pip:

```shell
pip install deflate_dict
```

## Deflating a dictionary

A dictionary will be deflated down to its smallest non-further iterable elements, defined as those not containing lists or dictionaries.

```python
from deflate_dict import deflate
D = {
    "a": [
        {
            "b": (0, 1, 2)
        },
        {
            "c": [1, 2, 3]
        }
    ]
}
result = deflate(D, sep="_")

# {'str(a)_listIndex(0)_str(b)': (0, 1, 2), 'str(a)_listIndex(1)_str(c)': [1, 2, 3]}
```

## Inflate a dictionary

To reinflate a dictionary to its forgotten glory, just go with:

```python
from deflate_dict import inflate
D = {"a_0_b": (0, 1, 2), "a_1_c": [1, 2, 3], "d": 4}

result = inflate(D, sep="_")

# {'a': [{'b': (0, 1, 2)}, {'c': [1, 2, 3]}], 'd': 4}
```

## Handling and restoring mixed types

To deflate and re-inflate mixed types and restore them to the original type you can use the `type_encode_key` keyword:

```python
from deflate_dict import deflate

D = {
    "a":[
        {
            "b":(0,1,2)
        },
        {
            "c": [1,2,3]
        }
    ]
}

print(deflate(D, sep="_", type_encode_key=False))

# {
# 'a_listIndex(0)_b': (0, 1, 2),
# 'a_listIndex(1)_c': [1, 2, 3]
# }

print(deflate(D, sep="_", type_encode_key=True))

# {
#    'str(a)_listIndex(0)_str(b)': (0, 1, 2),
#    'str(a)_listIndex(1)_str(c)': [1, 2, 3]
# }
```

## License

This software is distributed under MIT license.
