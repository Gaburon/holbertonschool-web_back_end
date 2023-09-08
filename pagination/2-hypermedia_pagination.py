#!/usr/bin/env python3
'''More pagination'''
import csv
import math
from typing import Tuple, List, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''Returns Tuple with start and final index'''
    start_index = (page - 1) * page_size
    final_index = page * page_size
    return (start_index, final_index)


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
        '''Returns a dataset page'''
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        self.dataset()
        index_tuple = index_range(page, page_size)
        return self.__dataset[index_tuple[0]: index_tuple[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        '''Returns a dataset dictionary'''
        data = self.get_page(page, page_size)
        page_size_return = len(data)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        next_page = page + 1 if total_pages > page else None
        prev_page = page - 1 if page > 1 else None
        ret_dict = {
            'page_size': page_size_return,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
        return ret_dict
