#!/usr/bin/env python3
"""Async Generation"""
from typing import List
import asyncio
import time

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """It returns a list"""
    list = [get(max_delay) for i in range(n)]
    return [await task for task in asyncio.as_completed(list)]
