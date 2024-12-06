from structure.node import Node


def get_middle_node_coords(nodes: list[Node]):
    x = sum([node.x for node in nodes]) / len(nodes)
    y = sum([node.y for node in nodes]) / len(nodes)
    return x, y