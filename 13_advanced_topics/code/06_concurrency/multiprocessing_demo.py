# 13_advanced_topics/code/06_concurrency/multiprocessing_demo.py

import multiprocessing
import time


def heavy_calculation(n: int) -> int:
    """CPU-bound task — sum of squares up to n."""
    return sum(i * i for i in range(n))


def run_sequential(numbers):
    start = time.time()
    results = [heavy_calculation(n) for n in numbers]
    print(f"Sequential took {time.time() - start:.2f}s")
    return results


def run_parallel(numbers):
    start = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(heavy_calculation, numbers)
    print(f"Parallel took {time.time() - start:.2f}s")
    return results


if __name__ == "__main__":
    numbers = [10_000_000] * 4

    run_sequential(numbers)
    run_parallel(numbers)