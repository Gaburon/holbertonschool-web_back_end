#!/usr/bin/env python3
"""Async Generation"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """It returns a delayed value """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
