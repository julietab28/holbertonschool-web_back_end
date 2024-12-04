#!/usr/bin/env python3
from typing import Union, Tuple
import math


def to_kv(k:str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes two arguments and returns a tuple with
    the arguments as elements of it
    """
    square: float = math.sqrt(v)
    return (k, float(square))
