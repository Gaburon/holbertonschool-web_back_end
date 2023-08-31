#!/usr/bin/env python3
'''Typed duck types'''


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Typed function for task 9'''
    return [(i, len(i)) for i in lst]