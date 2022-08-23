Deflate Dict
=========================================================================================
|pip| |downloads|

Python package to deflate and re-inflate dictionaries.

How do I install this package?
----------------------------------------------
As usual, just download it using pip:

.. code:: shell

    pip install deflate_dict

Deflating a dictionary
-------------------------------------------
A dictionary will be deflated down to its smallest non-further iterable elements, defined as those not containing lists or dictionaries.

.. code:: python

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
    result = deflate(D, sep="_")

    # {'a_0_b': (0, 1, 2), 'a_1_c': [1, 2, 3], 'd': 4}


Inflate a dictionary
---------------------------------------------
To reinflate a dictionary to its forgotten glory, just go with:

.. code:: python

    from deflate_dict import inflate
    D = {"a_0_b": (0, 1, 2), "a_1_c": [1, 2, 3], "d": 4}

    result = inflate(D, sep="_")

    # {'a': [{'b': (0, 1, 2)}, {'c': [1, 2, 3]}], 'd': 4}

Handling and restoring mixed types
----------------------------------------------
To deflate and re-inflate mixed types and restore them to the original type
you can use the `type_encode_key` keyword:

.. code:: python

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

    print(deflate(D, sep="_", type_encode_key=True))

    # {
    #    'str(a)_listIndex(0)_str(b)': (0, 1, 2),
    #    'str(a)_listIndex(1)_str(c)': [1, 2, 3]
    # }


.. |pip| image:: https://badge.fury.io/py/deflate-dict.svg
    :target: https://badge.fury.io/py/deflate-dict
    :alt: Pypi project

.. |downloads| image:: https://pepy.tech/badge/deflate-dict
    :target: https://pepy.tech/badge/deflate-dict
    :alt: Pypi total project downloads 