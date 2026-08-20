# 13_advanced_topics/code/05_type_hints/type_hints_protocol.py

from typing import Protocol


# Define a Protocol — any class with read() method
class Readable(Protocol):
    def read(self) -> str:
        """Any class with read() method."""
        ...


class Camera:
    def read(self) -> str:
        return "Camera image"


class Lidar:
    def read(self) -> str:
        return "Lidar point cloud"


class FileReader:
    def read(self) -> str:
        return "File content"


# This function accepts anything with read() method
def process_data(source: Readable) -> str:
    data = source.read()
    return f"Processed: {data}"


# All of these work — without common inheritance
print(process_data(Camera()))       # Processed: Camera image
print(process_data(Lidar()))        # Processed: Lidar point cloud
print(process_data(FileReader()))   # Processed: File content