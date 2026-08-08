# robot/__init__.py
# This file turns the 'robot' folder into a Python package.

# Re-export commonly used classes for easier access
from .sensors import Camera, Motor
from .navigation import PathPlanner

__all__ = ["Camera", "Motor", "PathPlanner"]
# from robot import * → only Camera, Motor, PathPlanner

__version__ = "0.1.0"