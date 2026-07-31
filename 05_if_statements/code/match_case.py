# 05_if_statements/code/match_case.py
# match-case — Python's switch equivalent (Python 3.10+)

command = "start"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "pause":
        print("Pausing...")
    case _:  # default case
        print(f"Unknown command: {command}")

# match with advanced pattern matching
point = (0, 5)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"On y-axis at y={y}")
    case (x, 0):
        print(f"On x-axis at x={x}")
    case (x, y):
        print(f"Point at ({x}, {y})")