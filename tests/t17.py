from plotting.plot import draw
from productions.p17 import P17
from structure.graph import Graph
from structure.hyperedge import HyperEdge
from structure.node import Node
from tests.test import Test
from util.calculations import get_middle_node_coords


class T17(Test):
    @staticmethod
    def run():
        # T17.case1()
        # T17.case2()
        # T17.case3()
        # T17.case4()
        T17.case5()

    @staticmethod
    def case1():
        g = Graph()

        n1 = Node(0, 0, "N1", False)
        n2 = Node(1, 0, "N2", False)
        n3 = Node(1, 1, "N3", False)
        n4 = Node(0, 1, "N4", False)
        n5 = Node((n2.x + n3.x) / 2, (n2.y + n3.y) / 2, "N5", True)
        n6 = Node(n3.x * 2, n5.y, "N6", False)
        n7 = Node(n3.x * 2, n3.y, "N7", False)
        n8 = Node((n1.x + n2.x) / 2, n1.y, "N8", False)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
            g.add_node(n)

        e1 = HyperEdge((n2, n5), 'E', False, False)
        e2 = HyperEdge((n5, n3), 'E', False, False)

        e3 = HyperEdge((n1, n2, n3, n4, n8), 'Q', False, False)
        e4 = HyperEdge((n3, n5, n6, n7), 'Q', False, True)

        for e in [e1, e2]:
            g.add_edge(e)

        for e in [e3, e4]:
            g.add_hyper_edge(e)

        draw(g)
        P17().apply(g)
        draw(g)

    @staticmethod
    def case2():
        g = Graph()

        n1 = Node(0, 0, "N1", False)
        n2 = Node(1, 0, "N2", False)
        n3 = Node(1, 1, "N3", False)
        n4 = Node(0, 1, "N4", False)
        n5 = Node((n2.x + n3.x) / 2, (n2.y + n3.y) / 2, "N5", True)
        n6 = Node(n3.x * 2, n5.y, "N6", False)
        n7 = Node(n3.x * 2, n3.y, "N7", False)
        n8 = Node((n1.x + n2.x) / 2, n1.y, "N8", False)

        n9 = Node((n1.x + n2.x) / 2, n4.y, "N9", False)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9]:
            g.add_node(n)

        e1 = HyperEdge((n2, n5), 'E', False, False)
        e2 = HyperEdge((n5, n3), 'E', False, False)

        e3 = HyperEdge((n1, n2, n3, n4, n8), 'Q', False, False)
        e4 = HyperEdge((n3, n5, n6, n7), 'Q', False, True)

        e5 = HyperEdge((n9, n8), 'E', False, False)

        for e in [e1, e2, e5]:
            g.add_edge(e)

        for e in [e3, e4]:
            g.add_hyper_edge(e)

        draw(g)
        P17().apply(g)
        draw(g)

    @staticmethod
    def case3():
        g = Graph()

        n1 = Node(0, 0, "N1", False)
        n2 = Node(1, 0, "N2", False)
        n3 = Node(1, 1, "N3", False)
        n4 = Node(0, 1, "N4", False)
        n5 = Node((n2.x + n3.x) / 2, (n2.y + n3.y) / 2, "N5", True)
        n6 = Node(n3.x * 2, n5.y, "N6", False)
        n7 = Node(n3.x * 2, n3.y, "N7", False)
        n8 = Node((n1.x + n2.x) / 2, n1.y, "N8", False)

        n9 = Node(-0.5, 1.5, "N9", False)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9]:
            g.add_node(n)

        e1 = HyperEdge((n2, n5), 'E', False, False)
        e2 = HyperEdge((n5, n3), 'E', False, False)

        e3 = HyperEdge((n1, n2, n3, n4, n8), 'Q', False, False)
        e4 = HyperEdge((n3, n5, n6, n7), 'Q', False, True)

        e5 = HyperEdge((n9, n4), 'E', False, False)

        for e in [e1, e2, e5]:
            g.add_edge(e)

        for e in [e3, e4]:
            g.add_hyper_edge(e)

        draw(g)
        P17().apply(g)
        draw(g)

    @staticmethod
    def case4():
        g = Graph()

        n1 = Node(0, 0, "N1", False)
        n2 = Node(1, 0, "N2", False)
        n3 = Node(1, 1, "N3", False)
        n4 = Node(0, 1, "N4", False)
        n5 = Node((n2.x + n3.x) / 2, (n2.y + n3.y) / 2, "N5", True)
        n6 = Node(n3.x * 2, n5.y, "N6", False)
        n7 = Node(n3.x * 2, n3.y, "N7", False)
        n8 = Node((n1.x + n2.x) / 2, n1.y, "N8", False)

        n9 = Node(-0.5, 1.5, "N9", False)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9]:
            g.add_node(n)

        e1 = HyperEdge((n2, n5), 'E', False, False)
        e2 = HyperEdge((n5, n3), 'E', False, False)

        e3 = HyperEdge((n1, n2, n3, n4, n8), 'Q', False, False)
        e4 = HyperEdge((n3, n5, n6, n7), 'Q', False, False)

        e5 = HyperEdge((n9, n4), 'E', False, False)

        for e in [e1, e2, e5]:
            g.add_edge(e)

        for e in [e3, e4]:
            g.add_hyper_edge(e)

        draw(g)
        P17().apply(g)
        draw(g)

    @staticmethod
    def case5():
        g = Graph()

        n1 = Node(0, 0, "N1", False)
        n2 = Node(1, 0, "N2", False)
        n3 = Node(1, 1, "N3", False)
        n4 = Node(0, 1, "N4", False)
        n5 = Node((n2.x + n3.x) / 2, (n2.y + n3.y) / 2, "N5", True)
        n6 = Node(n3.x * 2, n5.y, "N6", False)
        n7 = Node(n3.x * 2, n3.y, "N7", False)
        n8 = Node((n1.x + n2.x) / 2, n1.y, "N8", False)

        n9 = Node(-0.5, 1.5, "N9", False)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9]:
            g.add_node(n)

        e1 = HyperEdge((n2, n5), 'E', False, False)
        e2 = HyperEdge((n5, n3), 'E', False, False)

        e3 = HyperEdge((n1, n2, n3, n4, n8), 'Q', False, False)
        e4 = HyperEdge((n3, n5, n6, n7), 'Q', False, True)

        e5 = HyperEdge((n9, n4), 'E', False, False)
        e6 = HyperEdge((n9, n1), 'E', False, False)
        e7 = HyperEdge((n9, n3), 'E', False, False)
        e8 = HyperEdge((n3, n4), 'E', False, False)
        e9 = HyperEdge((n4, n1), 'E', False, False)
        e10 = HyperEdge((n1, n2), 'E', False, False)

        for e in [e1, e2, e5, e6, e7, e8, e9, e10]:
            g.add_edge(e)

        for e in [e3, e4]:
            g.add_hyper_edge(e)

        draw(g)
        P17().apply(g)
        draw(g)
