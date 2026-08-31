# 09_classes_oop/exercises/exercise_05.py
# Chapter 09 Exercise 5 — Composition

class Engine:
    """Engine component."""

    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")


class Robot:
    """Robot HAS-A Engine — not IS-A Engine."""

    def __init__(self, name):
        self.name = name
        self.engine = Engine()  # Composition — Robot has an Engine

    def power_on(self):
        print(f"{self.name}: ", end="")
        self.engine.start()

    def power_off(self):
        print(f"{self.name}: ", end="")
        self.engine.stop()


robot = Robot("R1")
robot.power_on()
robot.power_off()