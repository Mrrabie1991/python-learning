# 13_advanced_topics/code/05_type_hints/type_hints_literal.py

from typing import Literal


# Only "start", "stop", "pause" are allowed
def set_robot_status(status: Literal["start", "stop", "pause"]) -> str:
    return f"Robot status: {status}"


print(set_robot_status("start"))  # OK
print(set_robot_status("stop"))   # OK
# set_robot_status("invalid")     # Type checker: error!