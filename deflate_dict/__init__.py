from support_developer import support_luca
from .deflate import deflate
from .inflate import inflate

support_luca("deflate_dict")

__all__ = ["deflate", "inflate"]