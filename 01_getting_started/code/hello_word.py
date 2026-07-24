# hello_world.py
# The traditional first program — but with an engineering twist.

import sys
import platform

def main():
    print("Hello, Intelligent Systems!")
    print(f"Python version: {sys.version}")
    print(f"Running on: {platform.system()} {platform.release()}")

if __name__ == "__main__":
    main()