from dataclasses import dataclass
from structure.node import Node


@dataclass(frozen=True)
class HyperEdge:
    nodes: list[Node]
    label: str
    b: bool = False
    r: bool = False
