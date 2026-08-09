# robot.py — classes to test

class Camera:
    def __init__(self, resolution=(1920, 1080)):
        self.resolution = resolution

    def read(self):
        return f"Image at {self.resolution[0]}x{self.resolution[1]}"


class Motor:
    def __init__(self, max_speed=100):
        self.max_speed = max_speed
        self.current_speed = 0

    def set_speed(self, speed):
        self.current_speed = min(speed, self.max_speed)
        return self.current_speed