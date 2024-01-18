#!/usr/bin/env python3
""" coroutine called async_generator that takes no arguments.
    The coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10. Use the random module. """

from typing import Generator
import asyncio
import random

async def async_generator() -> Generator[float, None, None]:
    """A function that prints a random number
    between 0 and 10 after 1 second wait."""
    async for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
