from plotting.plot import draw
from productions.p5 import P5
from structure.graph import Graph
from structure.hyperedge import HyperEdge
from structure.node import Node
from tests.test import Test


class T5(Test):
    @staticmethod
    def run():
        g = Graph()
        n1 = Node(0, 0, "N1")
        n2 = Node(1, 0, "N2")
        n3 = Node(1, 1, "N3")
        n4 = Node(0, 1, "N4")
        n5 = Node(1, 0.5, "N5", True)
        n6 = Node(0.5, 0, "N6", True)
        n7 = Node(0, 0.5, "N7", True)

        for n in [n1, n2, n3, n4, n5, n6, n7]:
            g.add_node(n)

        edges = [
            (n1, n6), (n6, n2), (n2, n5), (n5, n3),
            (n3, n4), (n4, n7), (n7, n1)
        ]

        for u, v in edges:
            g.add_edge(HyperEdge((u, v), "E"))

        hyper_edge = HyperEdge((n1, n2, n3, n4), 'E', r=True)
        g.add_hyper_edge(hyper_edge)

        draw(g)
        P5().apply(g)
        draw(g)
        P5().apply(g)
        draw(g)