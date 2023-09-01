#!/usr/bin/env python3
"""Async Generation"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """It returns a list of all delayed tasks"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    delayed_tasks = [await task for task in asyncio.as_completed(tasks)]
    return delayed_tasks
