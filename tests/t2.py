from plotting.plot import draw
from productions.p2 import P2
from structure.graph import Graph
from structure.hyperedge import HyperEdge
from structure.node import Node
from tests.test import Test


class T2(Test):
    @staticmethod
    def run():
        T2.basic_positive()
        T2.positive_hanging_on_the_left()
        T2.negative_non_hanging()
        T2.positive_extra_edge()

    @staticmethod
    def basic_positive():
        g = Graph()
        n1 = Node(0, 0, "N1", False)
        n2 = Node(1, 0, "N2", False)
        n3 = Node(1, 1, "N3", False)
        n4 = Node(0, 1, "N4", False)
        n5 = Node(1, 0.5, "N5", True)
        e1 = HyperEdge((n1, n2), 'E', False, False)
        e2 = HyperEdge((n4, n3), 'E', True, False)
        e3 = HyperEdge((n2, n5), 'E', True, False)
        e4 = HyperEdge((n5, n3), 'E', True, False)
        e5 = HyperEdge((n4, n1), 'E', False, False)
        e6 = HyperEdge((n1, n2, n3, n4), 'E', False, True)
        g.add_node(n1)
        g.add_node(n2)
        g.add_node(n3)
        g.add_node(n4)
        g.add_node(n5)
        g.add_edge(e1)
        g.add_edge(e2)
        g.add_edge(e3)
        g.add_edge(e4)
        g.add_edge(e5)
        g.add_hyper_edge(e6)

        draw(g)
        P2().apply(g)
        draw(g)

    @staticmethod
    def positive_hanging_on_the_left():
        g = Graph()
        n1 = Node(0, 0, "N1", False)
        n2 = Node(1, 0, "N2", False)
        n3 = Node(1, 1, "N3", False)
        n4 = Node(0, 1, "N4", False)
        n5 = Node(0, 0.5, "N5", True)
        e1 = HyperEdge((n1, n2), 'E', False, False)
        e2 = HyperEdge((n2, n3), 'E', True, False)
        e3 = HyperEdge((n1, n5), 'E', True, False)
        e4 = HyperEdge((n5, n4), 'E', True, False)
        e5 = HyperEdge((n4, n3), 'E', False, False)
        e6 = HyperEdge((n1, n2, n3, n4), 'E', False, True)
        g.add_node(n1)
        g.add_node(n2)
        g.add_node(n3)
        g.add_node(n4)
        g.add_node(n5)
        g.add_edge(e1)
        g.add_edge(e2)
        g.add_edge(e3)
        g.add_edge(e4)
        g.add_edge(e5)
        g.add_hyper_edge(e6)

        draw(g)
        P2().apply(g)
        draw(g)

    @staticmethod
    def negative_non_hanging():
        g = Graph()
        n1 = Node(0, 0, "N1", False)
        n2 = Node(1, 0, "N2", False)
        n3 = Node(1, 1, "N3", False)
        n4 = Node(0, 1, "N4", False)
        n5 = Node(1, 0.5, "N5", False)
        e1 = HyperEdge((n1, n2), 'E', False, False)
        e2 = HyperEdge((n4, n3), 'E', True, False)
        e3 = HyperEdge((n2, n5), 'E', True, False)
        e4 = HyperEdge((n5, n3), 'E', True, False)
        e5 = HyperEdge((n4, n1), 'E', False, False)
        e6 = HyperEdge((n1, n2, n3, n4), 'E', False, True)
        g.add_node(n1)
        g.add_node(n2)
        g.add_node(n3)
        g.add_node(n4)
        g.add_node(n5)
        g.add_edge(e1)
        g.add_edge(e2)
        g.add_edge(e3)
        g.add_edge(e4)
        g.add_edge(e5)
        g.add_hyper_edge(e6)

        draw(g)
        P2().apply(g)
        draw(g)

    @staticmethod
    def positive_extra_edge():
        g = Graph()
        n1 = Node(0, 0, "N1", False)
        n2 = Node(1, 0, "N2", False)
        n3 = Node(1, 1, "N3", False)
        n4 = Node(0, 1, "N4", False)
        n5 = Node(1, 0.5, "N5", True)
        e1 = HyperEdge((n1, n2), 'E', False, False)
        e2 = HyperEdge((n4, n3), 'E', True, False)
        e3 = HyperEdge((n2, n5), 'E', True, False)
        e4 = HyperEdge((n5, n3), 'E', True, False)
        e5 = HyperEdge((n4, n1), 'E', False, False)
        e6 = HyperEdge((n1, n2, n3, n4), 'E', False, True)
        e7 = HyperEdge((n1, n5), 'E', False, False)
        g.add_node(n1)
        g.add_node(n2)
        g.add_node(n3)
        g.add_node(n4)
        g.add_node(n5)
        g.add_edge(e1)
        g.add_edge(e2)
        g.add_edge(e3)
        g.add_edge(e4)
        g.add_edge(e5)
        g.add_hyper_edge(e6)
        g.add_edge(e7)

        draw(g)
        P2().apply(g)
        draw(g)

