from dataclasses import dataclass


@dataclass(frozen=True)
class Node:
    x: float
    y: float
    label: str
    h: bool = False
    hyper: bool = False
    hyper_r: bool = False
