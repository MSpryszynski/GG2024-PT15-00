from plotting.plot import draw
from productions.p8 import P8
from structure.graph import Graph
from structure.hyperedge import HyperEdge
from structure.node import Node
from tests.test import Test


class T8(Test):
    @staticmethod
    def run():
        g = Graph()
        n1 = Node(0, 0, "N1")
        n2 = Node(1, 0, "N2")
        n3 = Node(1, 1, "N3")
        n4 = Node(0, 1, "N4")
        n5 = Node(1, 0.5, "N5", True)
        n6 = Node(2, 0.5, "N6")
        n7 = Node(2, 1, "N7")

        for n in [n1, n2, n3, n4, n5, n6, n7]:
            g.add_node(n)


        edges = [
            (n2, n5), (n5, n3)
        ]

        for u, v in edges:
            g.add_edge(HyperEdge((u, v), "E"))

        hyper_edges = [
            [(n1, n2, n3, n4), False], [(n5, n6, n7, n3), True]
        ]

        for nodes, r in hyper_edges:
            u, v, w, x = nodes
            g.add_hyper_edge(HyperEdge((u, v, w, x), "Q", r=r))

        draw(g)
        P8().apply(g)
        draw(g)
        P8().apply(g)
        draw(g)