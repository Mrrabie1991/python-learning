# 13_advanced_topics/code/04_context_managers/contextmanager_decorator.py

import time
from contextlib import contextmanager


@contextmanager
def timer():
    """Same Timer as above, but using yield — simpler."""
    start = time.time()
    print("Timer started")
    yield  # Code inside the 'with' block runs here
    print(f"Elapsed: {time.time() - start:.4f} seconds")


@contextmanager
def database_connection(config_path):
    """Database context manager using yield."""
    print(f"Connecting to database: {config_path}")
    # Setup
    db = {"connected": True}
    try:
        yield db  # db goes into 'as db'
    finally:
        # Cleanup — always runs
        print("Closing database connection")


# Usage
with timer():
    sum(range(10_000_000))

with database_connection("config.json") as db:
    print(f"Database: {db}")