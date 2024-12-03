#!/usr/bin/env python3
import math


def to_str(n: float) -> float:
    """
    Converts the integer part of a float into string

    This function takes an argument 'n', stracts the integer part
    of the float and converts the integer into string

    Args:
        n: float 
    """
    txt = math.floor(n)
    return str(txt)
