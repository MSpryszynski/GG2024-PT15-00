from plotting.plot import draw
from productions.p14 import P14
from structure.graph import Graph
from structure.hyperedge import HyperEdge
from structure.node import Node
from tests.test import Test
from util.calculations import get_middle_node_coords


class T14(Test):
    @staticmethod
    def run():
        g = Graph()
        n1 = Node(0, 0, "N1", False)
        n2 = Node(1, 0, "N2", False)
        n3 = Node(1, 1, "N3", False)
        n4 = Node(0, 1, "N4", False)
        n5 = Node(1.5, 0.5, "N5", False)

        x6, y6 = get_middle_node_coords([n1, n2])
        n6 = Node(x6, y6, "N6", True)
        x7, y7 = get_middle_node_coords([n1, n4])
        n7 = Node(x7, y7, "N7", True)
        x8, y8 = get_middle_node_coords([n4, n3])
        n8 = Node(x8, y8, "N8", True)
        x9, y9 = get_middle_node_coords([n5, n3])
        n9 = Node(x9, y9, "N9", True)

        e1 = HyperEdge((n1, n2), 'E', False, False)
        e2 = HyperEdge((n1, n4), 'E', False, False)
        e3 = HyperEdge((n2, n5), 'E', False, False)
        e4 = HyperEdge((n5, n9), 'E', False, False)
        e7 = HyperEdge((n9, n3), 'E', False, False)
        e5 = HyperEdge((n4, n3), 'E', False, False)
        e6 = HyperEdge((n1, n2, n3, n4, n5), 'E', False, True)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9]:
            g.add_node(n)

        g.add_edge(e1)
        g.add_edge(e2)
        g.add_edge(e3)
        g.add_edge(e4)
        g.add_edge(e5)
        g.add_edge(e7)
        g.add_hyper_edge(e6)

        draw(g)
        P14().apply(g)
        draw(g)
        P14().apply(g)
        draw(g)