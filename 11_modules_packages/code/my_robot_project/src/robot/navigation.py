# robot/navigation.py
# Navigation-related classes

# class PathPlanner:
#     def plan(self, start, goal):
#         return f"Path planned from {start} to {goal}"

# robot/navigation.py — updated with relative import

from .sensors import Camera  # . means this folder (robot/)

class PathPlanner:
    def __init__(self):
        self.camera = Camera()

    def plan(self, start, goal):
        image = self.camera.read()
        return f"Using {image} | Path from {start} to {goal}"

class Localizer:
    def get_position(self):
        return (0, 0)