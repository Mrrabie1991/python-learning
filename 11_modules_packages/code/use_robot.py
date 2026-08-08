# use_robot.py — using the robot package

# Method 1: import from package
from robot.sensors import Camera
cam = Camera()
print(cam.read())

# Method 2: import the package (access re-exports)
from robot import Motor
motor = Motor()
print(motor.set_speed(50))

# Method 3: import from submodule
from robot.navigation import PathPlanner
planner = PathPlanner()
print(planner.plan((0, 0), (10, 20)))