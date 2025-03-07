#!/usr/bin/env python3
"""
Pagination project
"""
from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function that returns a index range ofpages
    """
    page_i: int = (page - 1) * page_size
    page_f: int = page * page_size
    return (page_i, page_f)

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the elements of the page
        """
        assert isinstance(page, int) and isinstance(page_size, int), "must be an integer"
        assert page > 0 and page_size > 0, "must be grater than 0"
        
        page_i, page_f = index_range(page, page_size)
        return self.dataset()[page_i:page_f]
