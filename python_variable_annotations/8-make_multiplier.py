#!/usr/bin/env python3
"""
This module creates a function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function takes one argument of type float and
    returns a function

    Args:
        multiplier: float
    """
    def mult(value: float) -> float:
        """
        This function takes a value of type float and returns
        a multiplication of value and multiplier

        Args:
            value: float
        """
        return value * multiplier

    return mult
