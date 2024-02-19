#!/usr/bin/env python3
"""returns an async.Task"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """returns a type"""
    # task = asyncio.create_task(wait_random(max_delay))
    # return task
    return asyncio.Task(wait_random(max_delay))
