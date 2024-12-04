#!/usr/bin/env python3
from typing import Union
import math


def to_kv(k:str, v: Union[int, float]) -> tuple:
    """
    Takes two arguments and returns a tuple with
    the arguments as elements of it
    """
    square: float = math.sqrt(v)
    return (k, square)
