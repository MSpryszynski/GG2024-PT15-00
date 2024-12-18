from dataclasses import dataclass


@dataclass
class Node:
    x: float
    y: float
    label: str
    h: bool | None = False
    hyper: bool = False
    hyper_r: bool = False

    def __hash__(self):
        return hash((self.x, self.y, self.label))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.label == other.label
