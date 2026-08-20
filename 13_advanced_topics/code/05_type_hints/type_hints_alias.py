# 13_advanced_topics/code/05_type_hints/type_hints_alias.py

from typing import TypeAlias

# Type alias
Point: TypeAlias = tuple[float, float]
ScoreMap: TypeAlias = dict[str, int]
DataFrame: TypeAlias = list[list[float]]

def distance(p1: Point, p2: Point) -> float:
    """Calculate Euclidean distance between two points."""
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2) ** 0.5

def get_average(scores: ScoreMap) -> float:
    """Calculate average score from a score map."""
    return sum(scores.values()) / len(scores)

# Usage
p1: Point = (0.0, 0.0)
p2: Point = (3.0, 4.0)
print(distance(p1, p2))  # 5.0

scores: ScoreMap = {"Ali": 85, "Sara": 92}
print(get_average(scores))  # 88.5