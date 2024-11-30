from dataclasses import dataclass


@dataclass(frozen=True)
class Node:
    x: float
    y: float
    label: str
    h: bool = False
