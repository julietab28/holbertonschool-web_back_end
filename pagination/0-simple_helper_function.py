#!/usr/bin/env python3
"""
Pagination project
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function that returns a index range ofpages
    """
    page_i = (page - 1) * page_size
    page_f = page + page_size
    return (page_i, page_f)
    