#!/usr/bin/env python3
"""Async Tasks"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of delayed floats by using tasks"""
    tasks = [task_wait_random(max_delay) for i in range(n)]
    return [await t for t in asyncio.as_completed(tasks)]
