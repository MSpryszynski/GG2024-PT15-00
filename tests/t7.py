from plotting.plot import draw
from productions.p7 import P7
from structure.graph import Graph
from structure.hyperedge import HyperEdge
from structure.node import Node
from tests.test import Test


class T7(Test):
    @staticmethod
    def run():
        g = Graph()
        n1 = Node(0, 0, "N1", h=True)
        n2 = Node(1, 0, "N2")
        n3 = Node(1, 1, "N3")
        n4 = Node(0, 1, "N4")

        for n in [n1, n2, n3, n4]:
            g.add_node(n)

        g.add_hyper_edge(HyperEdge((n1, n2, n3, n4), "Q", r=False))

        draw(g)
        P7().apply(g)
        draw(g)

        g = Graph()
        n1 = Node(0, 0, "N1", h=True)
        n2 = Node(1, 0, "N2")
        n3 = Node(1, 1, "N3")
        n4 = Node(0, 1, "N4")
        n5 = Node(0, 2, "N5")

        for n in [n1, n2, n3, n4, n5]:
            g.add_node(n)

        g.add_hyper_edge(HyperEdge((n1, n2, n3, n4), "Q", r=False))
        g.add_edge(HyperEdge((n1, n2), "E", True))

        draw(g)
        P7().apply(g)
        draw(g)


        g = Graph()
        n1 = Node(0, 0, "N1", h=True)
        n2 = Node(1, 0, "N2")
        n3 = Node(1, 1, "N3")

        for n in [n1, n2, n3]:
            g.add_node(n)

        g.add_hyper_edge(HyperEdge((n1, n2, n3), "Q", r=False))
        HyperEdge((n2, n3), "E", True)
        draw(g)
        P7().apply(g)
        draw(g)


