# 13_advanced_topics/code/05_type_hints/type_hints_final.py

from typing import Final

# Constant — never reassign
MAX_SPEED: Final = 100
PI: Final = 3.14159

class Robot:
    # Constant in class
    DEFAULT_RESOLUTION: Final = (1920, 1080)
    
    def __init__(self):
        self.resolution = self.DEFAULT_RESOLUTION

# MAX_SPEED = 200  # Type checker: error! Cannot reassign Final