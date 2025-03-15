#!/usr/bin/env python3
"""
Pagination project
"""
from typing import Tuple
import csv
import math
from typing import List, Dict


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
    file = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.file) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the elements of the page
        """
        assert isinstance(page, int), "must be an integer"
        assert isinstance(page_size, int), "must be an integer"
        assert page > 0 and page_size > 0, "must be grater than 0"

        page_i, page_f = index_range(page, page_size)
        return self.dataset()[page_i:page_f]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        """
        Function that returns a dictionary with pagination info
        """
        total_pages: int = math.ceil(len(self.dataset()) / page_size) 
        next_page: int = page + 1 if page < total_pages else None
        prev_page: int = page - 1 if page > 1 else None
        return {
            "page_size": len(self.get_page(page, page_size)),
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }