#!/usr/bin/env python3
""" Complex types - list of floats and integers """
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Type annotated function that takes a list of float and integers
    and return their sum"""
    return sum(mxd_lst)
