# 13_advanced_topics/code/06_concurrency/threading_demo.py

import threading
import time


def download_file(file_id: int) -> str:
    """Simulate downloading a file (I/O-bound)."""
    print(f"  Downloading file {file_id}...")
    time.sleep(1)  # Simulate network delay (GIL released during sleep)
    return f"file_{file_id}.dat"


def download_all():
    """Download 5 files concurrently using threads."""
    threads = []
    results = []

    def worker(file_id: int):
        result = download_file(file_id)
        results.append(result)

    # Create and start threads
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    return results


# Compare: sequential vs threaded
print("Sequential:")
start = time.time()
for i in range(5):
    download_file(i)
print(f"Sequential took {time.time() - start:.2f}s\n")

print("Threaded:")
start = time.time()
results = download_all()
print(f"Threaded took {time.time() - start:.2f}s")