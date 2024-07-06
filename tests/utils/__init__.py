"""Utility functions for tests"""
import json


def match(d1, d2):
    """Check if two dictionaries are equal"""
    return json.dumps(d1, sort_keys=True) == json.dumps(d2, sort_keys=True)


test_dict = {
    "z": 4,
    "a": [
        [{"b": (2, 3), "c": {"d": ["dd", "dd"]}}],
        [{"b": (2, 3), "c": {"d": ["dd", "dd"]}}],
    ],
}
