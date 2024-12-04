#!/usr/bin/env python3
from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    This function takes a list of float as an argument and
    return the sum of all the elements of the list as a float

    Args:
        input_list: list
    """
    nums: float = 0.0
    for num in input_list:
        nums += num
    return nums
