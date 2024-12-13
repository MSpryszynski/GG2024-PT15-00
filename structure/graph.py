import networkx as nx

from structure.hyperedge import HyperEdge
from structure.node import Node


class Graph:
    def __init__(self):
        self.ordered_nodes: list[Node] = []
        self.dict_edges: dict[(str, str), HyperEdge] = dict()
        self._G = nx.Graph()

    def add_node(self, node: Node) -> None:
        self._G.add_node(node, h=node.h, hyper_r=node.hyper_r)
        if node not in self.ordered_nodes:
            self.ordered_nodes.append(node)

    def remove_node(self, node: Node):
        self._G.remove_node(node)
        self.ordered_nodes.remove(node)

    def get_nodes(self):
        return self._G.nodes

    def add_edge(self, edge: HyperEdge):
        u, v = edge.nodes
        self._G.add_edge(u, v)
        self.dict_edges[(u.label, v.label)] = edge
        self.dict_edges[(v.label, u.label)] = edge

    def add_hyper_edge(self, edge: HyperEdge):
        nodes = edge.nodes
        x = sum([node.x for node in nodes]) / len(nodes)
        y = sum([node.y for node in nodes]) / len(nodes)
        hyper_node = Node(x, y, f"Q-{x}-{y}", False, True, edge.r)
        self.add_node(hyper_node)
        for node in edge.nodes:
            he = HyperEdge([hyper_node, node], f"{hyper_node.label}-{node.label}")
            self.add_edge(he)

    def get_edge(self, u: Node, v: Node) -> HyperEdge:
        return self.dict_edges[(u.label, v.label)]

    def remove_edge(self, u: Node, v: Node):
        self._G.remove_edge(u, v)
        del self.dict_edges[(u.label, v.label)]
        del self.dict_edges[(v.label, u.label)]

    def get_edges(self):
        return self._G.edges

    def get(self):
        return self._G
