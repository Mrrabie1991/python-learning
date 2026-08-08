# robot/sensors.py
# Sensor-related classes

class Camera:
    def __init__(self, resolution=(1920, 1080)):
        self.resolution = resolution

    def read(self):
        return f"Camera: image at {self.resolution}"

class Motor:
    def __init__(self, max_speed=100):
        self.max_speed = max_speed

    def set_speed(self, speed):
        return f"Motor: speed set to {min(speed, self.max_speed)}"