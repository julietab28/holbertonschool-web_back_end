#!/usr/bin/env python3
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function take one argument of type list that
    contains ints and floats and return the sum of
    all elements

    Args:
        mxd_lst: List
    """
    nums: float = 0.0
    for num in mxd_lst:
        nums += num
    return nums
