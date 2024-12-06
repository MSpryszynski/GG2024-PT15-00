from dataclasses import dataclass
from typing import Set
from structure.node import Node


@dataclass(frozen=True)
class HyperEdge:
    nodes: Set[Node]
    label: str
    b: bool = False
    r: bool = False
