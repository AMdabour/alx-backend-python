#!/usr/bin/env python3
"""an async coroutine that waits for a delay num and eventually returns it"""
import asyncio
import random


async def wait_random(max_delay=10):
    """waits for the delay num and returns it"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
