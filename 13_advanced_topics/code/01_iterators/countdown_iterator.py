# 13_advanced_topics/code/01_iterators/countdown_iterator.py

class Countdown:
    """Iterator that counts down from n to 1."""

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        """Return the iterator object (self)."""
        return self

    def __next__(self):
        """Return next value or raise StopIteration."""
        if self.current <= 0:
            raise StopIteration  # Signal the for loop to stop
        value = self.current
        self.current -= 1
        return value


# Usage in a for loop
for num in Countdown(5):
    print(num)
# 5
# 4
# 3
# 2
# 1