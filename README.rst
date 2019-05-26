Deflate Dictionaries
==========================================================
|travis| |sonar_quality| |sonar_maintainability| |sonar_coverage| |code_climate_maintainability| |pip|

Python package to deflate and re-inflate dictionaries.

How do I get this?
-------------------------------------------
As usual, just get it from pip:

.. code:: bash

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
            "c": [1,2,3]
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


.. |travis| image:: https://travis-ci.org/LucaCappelletti94/deflate_dict.png
   :target: https://travis-ci.org/LucaCappelletti94/deflate_dict

.. |sonar_quality| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_deflate_dict&metric=alert_status
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_deflate_dict

.. |sonar_maintainability| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_deflate_dict&metric=sqale_rating
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_deflate_dict

.. |sonar_coverage| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_deflate_dict&metric=coverage
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_deflate_dict

.. |code_climate_maintainability| image:: https://api.codeclimate.com/v1/badges/25fb7c6119e188dbd12c/maintainability
   :target: https://codeclimate.com/github/LucaCappelletti94/deflate_dict/maintainability
   :alt: Maintainability

.. |pip| image:: https://badge.fury.io/py/deflate_dict.svg
    :target: https://badge.fury.io/py/deflate_dict