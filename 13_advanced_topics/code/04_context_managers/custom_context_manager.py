# 13_advanced_topics/code/04_context_managers/custom_context_manager.py

import time

class Timer:
    """Measure execution time of a code block."""

    def __enter__(self):
        # Runs when entering the 'with' block
        self.start = time.time()
        return self  # This value goes into 'as t'

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Runs when exiting the 'with' block (always, even on error)
        elapsed = time.time() - self.start
        print(f"Elapsed: {elapsed:.4f} seconds")
        # Return False = re-raise any exception that occurred
        return False

    def current_elapsed(self):
        # Utility method usable inside the with block
        return time.time() - self.start


# Usage
with Timer() as t:
    # Heavy work
    sum(range(10_000_000))
    print(f"Mid-block: {t.current_elapsed():.4f}s")