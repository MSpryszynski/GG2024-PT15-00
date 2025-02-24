from structure.graph import Graph
from productions.production import Production
from structure.node import Node
from structure.hyperedge import HyperEdge


class P7(Production):
    @staticmethod
    def left_side() -> Graph:
        g = Graph()
        n1 = Node(1, 1, "N1", h=None)
        n2 = Node(2, 1, "N2", h=None)
        n3 = Node(2, 2, "N3", h=None)
        n4 = Node(1, 2, "N4", h=None)
        for n in [n1, n2, n3, n4]:
            g.add_node(n)

        g.add_hyper_edge(HyperEdge((n1, n2, n3, n4), "Q", r=False))

        return g

    @staticmethod
    def right_side(iso_ordered_nodes, boundary_map):
        n1, n2, n3, n4, q = iso_ordered_nodes
        g = Graph()

        for n in [n1, n2, n3, n4]:
            g.add_node(n)

        g.add_hyper_edge(HyperEdge((n1, n2, n3, n4), "Q", r=True))

        return g
