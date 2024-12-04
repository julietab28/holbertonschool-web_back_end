#!/usr/bin/env python3
from typing import List, Iterable, Sequence, Tuple
"""
This module creates a function element_length
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This function takes a list(an Iterable )that contains
    Sequences(str, list, tuple, etc) and retruns a list that contains
    tuples that contains sequences and int

    Args:
        lst: Iterable[Sequence]
    """
    return [(i, len(i)) for i in lst]