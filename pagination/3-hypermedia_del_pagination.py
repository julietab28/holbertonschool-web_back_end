#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Funcion que returna un diccionario con la informacion de la pagina        
        """
        assert isinstance(index, int)
        assert index >= 0 and index < len(self.indexed_dataset())

        assert isinstance(page_size, int)

        data = []
        new_index = index
        i_dataset = self.indexed_dataset()
        count = 0
   
        while count < page_size and new_index in i_dataset:
            data.append(i_dataset[new_index])
            count += 1
            new_index += 1
        next_index = new_index
        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data,
        }
