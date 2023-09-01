#!/usr/bin/env python3
""" typing and asyncio """
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns list of delayed tasks"""
    results: List[float] = [task_wait_random(
        max_delay) for _ in range(n)]
    return [await result for result in asyncio.as_completed(results)]
