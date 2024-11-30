import networkx as nx

from structure.edge import Edge
from structure.node import Node


class Graph:
    def __init__(self):
        self.ordered_nodes: list[Node] = []
        self._G = nx.Graph()

    def add_node(self, node: Node) -> None:
        self._G.add_node(node)
        self.ordered_nodes.append(node)

    def get_nodes(self):
        return self._G.nodes

    def add_edge(self, edge: Edge):
        u, v = edge.nodes
        self._G.add_edge(u, v)

    def remove_edge(self, u: Node, v: Node):
        self._G.remove_edge(u, v)

    def get_edges(self):
        return self._G.edges

    def get(self):
        return self._G
