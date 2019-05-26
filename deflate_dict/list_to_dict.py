from typing import Dict, List

def list_to_dict(my_list:List)->Dict:
    """Return dictionary representing list values with corresponding keys values."""
    return dict(enumerate(my_list))