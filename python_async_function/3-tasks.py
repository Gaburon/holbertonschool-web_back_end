#!/usr/bin/env python3
"""First Async and Await corroutine"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    ''''Return a task made from wait_random'''
    task = asyncio.create_task(wait_random())
    return task
