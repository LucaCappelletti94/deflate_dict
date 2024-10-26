"""Utilities for encoding and decoding data types and structures."""

from deflate_dict.utils.is_iterable import is_iterable
from deflate_dict.utils.type_encoding import type_decode, type_encode
from deflate_dict.utils.list_encoding import encode_list, is_encoded_list, decode_list

__all__ = [
    "is_iterable",
    "type_decode",
    "type_encode",
    "encode_list",
    "is_encoded_list",
    "decode_list",
]
