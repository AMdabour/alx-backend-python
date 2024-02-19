#!/usr/bin/env python3
"""module"""
import asyncio
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure elapsed time and returns total_time / n"""
    start = time()
    asyncio.run(wait_n(n, max_delay))
    end = time()
    total = end - start
    return total / n
