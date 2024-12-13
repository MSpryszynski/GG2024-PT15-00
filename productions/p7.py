from structure.graph import Graph
from productions.production import Production
from structure.node import Node
from structure.hyperedge import HyperEdge


class P7(Production):
    @staticmethod
    def left_side() -> Graph:
        g = Graph()
        n1 = Node(1, 1, "N1")
        n2 = Node(2, 1, "N2")
        n3 = Node(2, 2, "N3")
        n4 = Node(1, 2, "N4")
        for n in [n1, n2, n3, n4]:
            g.add_node(n)

        g.add_hyper_edge(HyperEdge((n1, n2, n3, n4), "Q", r=False))

        return g

    @staticmethod
    def right_side(left: Graph):
        n1, n2, n3, n4, q = left.ordered_nodes
        g = Graph()

        for n in [n1, n2, n3, n4]:
            g.add_node(n)

        g.add_hyper_edge(HyperEdge((n1, n2, n3, n4), "Q", r=True))

        return g
