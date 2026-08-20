# 13_advanced_topics/code/05_type_hints/type_hints_typeddict.py

from typing import TypedDict


class Person(TypedDict):
    """Structure of a person dict."""
    name: str
    age: int
    city: str


class RobotConfig(TypedDict):
    """Robot configuration structure."""
    camera_resolution: tuple[int, int]
    max_speed: int
    sensors: list[str]


def create_person(name: str, age: int, city: str) -> Person:
    return {"name": name, "age": age, "city": city}


def configure_robot(config: RobotConfig) -> str:
    return f"Robot configured: {config['camera_resolution']}, max speed: {config['max_speed']}"


# Usage
person = create_person("Ali", 25, "Tehran")
print(person["name"])  # Ali

config = RobotConfig(
    camera_resolution=(1920, 1080),
    max_speed=100,
    sensors=["camera", "lidar"],
)
print(configure_robot(config))