#!/usr/bin/env python3
'''Index range'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''Returns Tuple with start and final index'''
    start_index = (page - 1) * page_size
    final_index = page * page_size
    return (start_index, final_index)
