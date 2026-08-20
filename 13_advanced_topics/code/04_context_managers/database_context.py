# 13_advanced_topics/code/04_context_managers/database_context.py

class DatabaseConnection:
    """Simulate a database connection with context manager."""

    def __init__(self, config_path):
        self.config_path = config_path
        self.connected = False

    def __enter__(self):
        # Setup — when entering 'with'
        print(f"Connecting to database with config: {self.config_path}")
        self.connected = True
        return self  # Goes into 'as db'

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Cleanup — when exiting 'with' (always runs)
        print("Closing database connection")
        self.connected = False
        # If an exception occurred, its info is here
        if exc_type is not None:
            print(f"Exception occurred: {exc_type.__name__}: {exc_val}")
        # False = re-raise the exception (don't suppress it)
        return False

    def query(self, sql):
        if not self.connected:
            raise RuntimeError("Not connected!")
        print(f"Executing: {sql}")
        return [{"id": 1, "name": "Ali"}]


# Usage
with DatabaseConnection("config.json") as db:
    result = db.query("SELECT * FROM users")
    print(f"Result: {result}")