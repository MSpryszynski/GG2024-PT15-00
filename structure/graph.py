import networkx as nx

from structure.hyperedge import HyperEdge
from structure.node import Node


class Graph:
    def __init__(self, is_main=False):
        self.ordered_nodes: list[Node] = []
        self._G = nx.Graph()
        self.is_main = is_main
        self.counter = 1

    def add_node(self, node: Node) -> None:
        if not node.label and self.is_main:
            node.label = f"N{self.counter}"
            self.counter += 1
        self._G.add_node(node, h=node.h, hyper_r=node.hyper_r, hyper=node.hyper)
        self.ordered_nodes.append(node)

    def remove_node(self, node: Node):
        self._G.remove_node(node)

    def get_nodes(self):
        return self._G.nodes

    def add_edge(self, edge: HyperEdge):
        u, v = edge.nodes
        self._G.add_edge(u, v, boundary=edge.b)

    def add_hyper_edge(self, edge: HyperEdge):
        nodes = edge.nodes
        x = sum([node.x for node in nodes]) / len(nodes)
        y = sum([node.y for node in nodes]) / len(nodes)
        hyper_node = Node(x, y, "Q", False, True, edge.r)
        self.add_node(hyper_node)
        for node in edge.nodes:
            self._G.add_edge(hyper_node, node, boundary=False)

    def remove_edge(self, u: Node, v: Node):
        self._G.remove_edge(u, v)

    def get_edges(self):
        return self._G.edges

    def get(self):
        return self._G
