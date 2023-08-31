#!/usr/bin/env python3
'''Typed lists'''


from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    '''Sums a mixed list'''
    return sum(input_list)