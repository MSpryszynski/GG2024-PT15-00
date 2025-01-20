from plotting.plot import draw
from productions.p11 import P11
from structure.graph import Graph
from structure.hyperedge import HyperEdge
from structure.node import Node
from tests.test import Test
from util.calculations import get_middle_node_coords


class T11(Test):
    @staticmethod
    def run():
        # T11.case1()
        # T11.case2()
        # T11.case3()
        # T11.case4()
        T11.case5()
    @staticmethod
    def case1():
        g = Graph()
        n1 = Node(0, 0, "N1", False)
        n2 = Node(1, 0, "N2", False)
        n3 = Node(1, 1, "N3", False)
        n4 = Node(0, 1, "N4", False)
        n5 = Node(1.5, 0.5, "N5", False)

        x6, y6 = get_middle_node_coords([n1, n2])
        n6 = Node(x6, y6, "N6", h=True)
        x7, y7 = get_middle_node_coords([n1, n4])
        n7 = Node(x7, y7, "N7", h=True)

        e1 = HyperEdge((n1, n6), 'E', False, False)
        e2 = HyperEdge((n6, n2), 'E', False, False)
        e3 = HyperEdge((n2, n5), 'E', False, False)
        e4 = HyperEdge((n5, n3), 'E', False, False)
        e5 = HyperEdge((n3, n4), 'E', False, False)
        e6 = HyperEdge((n4, n7), 'E', False, False)
        e7 = HyperEdge((n7, n1), 'E', False, False)
        e8 = HyperEdge((n1, n2, n3, n4, n5), 'Q', False, True)

        for n in [n1, n2, n3, n4, n5, n6, n7]:
            g.add_node(n)

        g.add_edge(e1)
        g.add_edge(e2)
        g.add_edge(e3)
        g.add_edge(e4)
        g.add_edge(e5)
        g.add_edge(e6)
        g.add_edge(e7)
        g.add_hyper_edge(e8)

        draw(g)
        P11().apply(g)
        draw(g)

    @staticmethod
    def case2():
        g = Graph()
        n1 = Node(0, 0, "N1", False)
        n2 = Node(1, 0, "N2", False)
        n3 = Node(1, 1, "N3", False)
        n4 = Node(0, 1, "N4", False)
        n5 = Node(1.5, 0.5, "N5", False)

        x6, y6 = get_middle_node_coords([n1, n2])
        n6 = Node(x6, y6, "N6", h=True)
        x7, y7 = get_middle_node_coords([n1, n4])
        n7 = Node(x7, y7, "N7", h=True)

        n8 = Node(0, 1.5, "N8", False)
        n9 = Node(1, 1.5, "N9", False)
        n10 = Node(0, -0.5, "N10", False)
        n11 = Node(1, -0.5, "N11", False)

        e1 = HyperEdge((n1, n6), 'E', False, False)
        e2 = HyperEdge((n6, n2), 'E', False, False)
        e3 = HyperEdge((n2, n5), 'E', False, False)
        e4 = HyperEdge((n5, n3), 'E', False, False)
        e5 = HyperEdge((n3, n4), 'E', False, False)
        e6 = HyperEdge((n4, n7), 'E', False, False)
        e7 = HyperEdge((n7, n1), 'E', False, False)
        e8 = HyperEdge((n1, n2, n3, n4, n5), 'Q', False, True)

        e9 = HyperEdge((n4, n8), 'E', False, False)
        e10 = HyperEdge((n8, n9), 'E', False, False)
        e11 = HyperEdge((n9, n3), 'E', False, False)
        e12 = HyperEdge((n2, n11), 'E', False, False)
        e13 = HyperEdge((n11, n10), 'E', False, False)
        e14 = HyperEdge((n10, n1), 'E', False, False)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11]:
            g.add_node(n)

        g.add_edge(e1)
        g.add_edge(e2)
        g.add_edge(e3)
        g.add_edge(e4)
        g.add_edge(e5)
        g.add_edge(e6)
        g.add_edge(e7)
        g.add_hyper_edge(e8)

        g.add_edge(e9)
        g.add_edge(e10)
        g.add_edge(e11)
        g.add_edge(e12)
        g.add_edge(e13)
        g.add_edge(e14)


        draw(g)
        P11().apply(g)
        draw(g)

    @staticmethod
    def case3():
        g = Graph()
        n1 = Node(0, 0, "N1", False)
        n2 = Node(1, 0, "N2", False)
        n3 = Node(1, 1, "N3", False)
        n4 = Node(0, 1, "N4", False)
        n5 = Node(1.5, 0.5, "N5", False)

        x6, y6 = get_middle_node_coords([n1, n2])
        n6 = Node(x6, y6, "N6", h=True)
        x7, y7 = get_middle_node_coords([n1, n4])
        n7 = Node(x7, y7, "N7", h=True)

        n8 = Node(0, 1.5, "N8", False)
        n9 = Node(1, 1.5, "N9", False)
        n10 = Node(0, -0.5, "N10", False)
        n11 = Node(1, -0.5, "N11", False)

        e1 = HyperEdge((n1, n6), 'E', False, False)
        e2 = HyperEdge((n6, n2), 'E', False, False)
        e3 = HyperEdge((n2, n5), 'E', False, False)
        e4 = HyperEdge((n5, n3), 'E', False, False)
        e5 = HyperEdge((n3, n4), 'E', False, False)
        e6 = HyperEdge((n4, n7), 'E', False, False)
        e7 = HyperEdge((n7, n1), 'E', False, False)
        e8 = HyperEdge((n1, n2, n3, n4, n5), 'Q', False, False)

        e9 = HyperEdge((n4, n8), 'E', False, False)
        e10 = HyperEdge((n8, n9), 'E', False, False)
        e11 = HyperEdge((n9, n3), 'E', False, False)
        e12 = HyperEdge((n2, n11), 'E', False, False)
        e13 = HyperEdge((n11, n10), 'E', False, False)
        e14 = HyperEdge((n10, n1), 'E', False, False)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11]:
            g.add_node(n)

        g.add_edge(e1)
        g.add_edge(e2)
        g.add_edge(e3)
        g.add_edge(e4)
        g.add_edge(e5)
        g.add_edge(e6)
        g.add_edge(e7)
        g.add_hyper_edge(e8)

        g.add_edge(e9)
        g.add_edge(e10)
        g.add_edge(e11)
        g.add_edge(e12)
        g.add_edge(e13)
        g.add_edge(e14)

        draw(g)
        P11().apply(g)
        draw(g)

    @staticmethod
    def case4():
        g = Graph()
        n1 = Node(0, 0, "N1", False)
        n2 = Node(1, 0, "N2", False)
        n3 = Node(1, 1, "N3", False)
        n4 = Node(0, 1, "N4", False)
        n5 = Node(1.5, 0.5, "N5", False)

        x6, y6 = get_middle_node_coords([n1, n2])
        n6 = Node(x6, y6, "N6", h=True)
        x7, y7 = get_middle_node_coords([n1, n4])
        n7 = Node(x7, y7, "N7", h=True)

        n8 = Node(0, 1.5, "N8", False)
        n9 = Node(1, 1.5, "N9", False)
        n10 = Node(0, -0.5, "N10", False)
        n11 = Node(1, -0.5, "N11", False)

        e1 = HyperEdge((n1, n6), 'E', False, False)
        e2 = HyperEdge((n6, n2), 'E', False, False)

        e4 = HyperEdge((n5, n3), 'E', False, False)
        e5 = HyperEdge((n3, n4), 'E', False, False)
        e6 = HyperEdge((n4, n7), 'E', False, False)
        e7 = HyperEdge((n7, n1), 'E', False, False)
        e8 = HyperEdge((n1, n2, n3, n4, n5), 'Q', False, True)

        e9 = HyperEdge((n4, n8), 'E', False, False)
        e10 = HyperEdge((n8, n9), 'E', False, False)
        e11 = HyperEdge((n9, n3), 'E', False, False)
        e12 = HyperEdge((n2, n11), 'E', False, False)
        e13 = HyperEdge((n11, n10), 'E', False, False)
        e14 = HyperEdge((n10, n1), 'E', False, False)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11]:
            g.add_node(n)

        g.add_edge(e1)
        g.add_edge(e2)

        g.add_edge(e4)
        g.add_edge(e5)
        g.add_edge(e6)
        g.add_edge(e7)
        g.add_hyper_edge(e8)

        g.add_edge(e9)
        g.add_edge(e10)
        g.add_edge(e11)
        g.add_edge(e12)
        g.add_edge(e13)
        g.add_edge(e14)

        draw(g)
        P11().apply(g)
        draw(g)

    @staticmethod
    def case5():
        g = Graph()
        n1 = Node(0, 0, "N1", False)
        n2 = Node(1, 0, "N2", False)
        n3 = Node(1, 1, "N3", False)
        n4 = Node(0, 1, "N4", False)
        n5 = Node(1.5, 0.5, "N5", False)

        n11 = Node(0, 1.5, "N11", False)
        n12 = Node(0, 2, "N12", False)
        n13 = Node(1, 2, "N13", False)
        n14 = Node(1.5, 1.5, "N14", False)
        n15 = Node(0.5, 1, "N15", False)

        x6, y6 = get_middle_node_coords([n1, n2])
        n6 = Node(x6, y6, "N6", h=True)
        x7, y7 = get_middle_node_coords([n1, n4])
        n7 = Node(x7, y7, "N7", h=True)

        e1 = HyperEdge((n1, n6), 'E', False, False)
        e2 = HyperEdge((n6, n2), 'E', False, False)
        e3 = HyperEdge((n2, n5), 'E', False, False)
        e4 = HyperEdge((n5, n3), 'E', False, False)
        e5 = HyperEdge((n3, n4), 'E', False, False)
        e6 = HyperEdge((n4, n7), 'E', False, False)
        e7 = HyperEdge((n7, n1), 'E', False, False)
        e8 = HyperEdge((n1, n2, n3, n4, n5), 'Q', False, True)

        e10 = HyperEdge((n4, n11), 'E', False, False)
        e11 = HyperEdge((n11, n12), 'E', False, False)
        e12 = HyperEdge((n12, n13), 'E', False, False)
        e13 = HyperEdge((n13, n14), 'E', False, False)
        e14 = HyperEdge((n14, n3), 'E', False, False)
        e15 = HyperEdge((n3, n15), 'E', False, False)
        e16 = HyperEdge((n15, n4), 'E', False, False)
        e17 = HyperEdge((n4, n3, n13, n12, n14), 'Q', False, True)

        for n in [n1, n2, n3, n4, n5, n6, n7, n11, n12, n13, n14, n15]:
            g.add_node(n)

        g.add_edge(e1)
        g.add_edge(e2)
        g.add_edge(e3)
        g.add_edge(e4)
        g.add_edge(e5)
        g.add_edge(e6)
        g.add_edge(e7)
        g.add_edge(e10)
        g.add_edge(e11)
        g.add_edge(e12)
        g.add_edge(e13)
        g.add_edge(e14)
        g.add_edge(e15)
        g.add_edge(e16)

        g.add_hyper_edge(e8)
        g.add_hyper_edge(e17)

        draw(g)
        P11().apply(g)
        draw(g)