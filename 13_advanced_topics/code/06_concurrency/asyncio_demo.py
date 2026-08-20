# 13_advanced_topics/code/06_concurrency/asyncio_demo.py

import asyncio
import time


async def download_file(file_id: int) -> str:
    """Simulate downloading a file (I/O-bound) with asyncio."""
    print(f"  Downloading file {file_id}...")
    await asyncio.sleep(1)  # GIL released — other tasks run
    return f"file_{file_id}.dat"


async def download_all():
    """Download 5 files concurrently."""
    tasks = [download_file(i) for i in range(5)]
    results = await asyncio.gather(*tasks)
    return results


# Run the async function
async def main():
    start = time.time()
    results = await download_all()
    print(f"Async took {time.time() - start:.2f}s")
    print(f"Results: {results}")


# Entry point for asyncio
asyncio.run(main())