from typing import Dict, List

def dict_to_list(my_dict:Dict)->List:
    """Return list representing dict values with corresponding keys values."""
    return [my_dict[k] for k in range(max(my_dict)+1)]