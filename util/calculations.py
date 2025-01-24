from structure.node import Node
from structure.graph import Graph
from math import inf


def get_middle_node_coords(nodes: list[Node]):
    x = sum([node.x for node in nodes]) / len(nodes)
    y = sum([node.y for node in nodes]) / len(nodes)
    return x, y


def get_closest_node(coords, graph: Graph):
    x, y = coords
    closest = inf
    curr_node = None

    for node in graph.get_nodes():
        dist = (node.x - x)**2 + (node.y - y)**2
        if dist < closest:
            curr_node = node
            closest = dist
    return curr_node