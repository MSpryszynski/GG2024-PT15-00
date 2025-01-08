import math
from plotting.plot import draw
from productions.p9 import P9
from structure.graph import Graph
from structure.hyperedge import HyperEdge
from structure.node import Node
from tests.test import Test

class T9(Test):
    @staticmethod
    def run():
        T9.case1()
        T9.case2()
        T9.case3()
        T9.case4()
        T9.case5()

    @staticmethod
    def case1():
        g = Graph()

        # Create nodes
        nodes = [
            Node(0, 0, "N1", False),
            Node(1, 0, "N2", False),
            Node(1, 1, "N3", False),
            Node(0, 1, "N4", False),
            Node(1.5, 0.5, "N5", False)
        ]

        for n in nodes:
            g.add_node(n)

        # Create edges
        edges = [
            (nodes[0], nodes[1]),
            (nodes[1], nodes[4]),
            (nodes[2], nodes[4]),
            (nodes[3], nodes[2]),
            (nodes[0], nodes[3]),
        ]

        for u, v in edges:
            g.add_edge(HyperEdge((u, v), "E"))

        # Create the hyperedge for the production
        hyperedge = HyperEdge((nodes[0], nodes[1], nodes[2], nodes[3], nodes[4]), "P", r=True)
        g.add_hyper_edge(hyperedge)

        draw(g)
        P9().apply(g)
        draw(g)

    @staticmethod
    def case2():
        g = Graph()

        # Create nodes
        nodes = [
            Node(0, 0, "N1", False),
            Node(1, 0, "N2", False),
            Node(1, 1, "N3", False),
            Node(0, 1, "N4", False),
            Node(1.5, 0.5, "N5", False)
        ]

        for n in nodes:
            g.add_node(n)

        # Create edges
        edges = [
            (nodes[0], nodes[1]),
            (nodes[1], nodes[4]),
            (nodes[2], nodes[4]),
            (nodes[3], nodes[2]),
            (nodes[0], nodes[3]),
        ]

        for u, v in edges:
            g.add_edge(HyperEdge((u, v), "E"))

        # Create the hyperedge for the production
        hyperedge = HyperEdge((nodes[0], nodes[1], nodes[2], nodes[3], nodes[4]), "P", r=False)
        g.add_hyper_edge(hyperedge)

        draw(g)
        P9().apply(g)
        draw(g)

    @staticmethod
    def case3():
        g = Graph()

        # Create nodes
        nodes = [
            Node(0, 0, "N1", False),
            Node(1, 0, "N2", False),
            Node(1, 1, "N3", False),
            Node(0, 1, "N4", False),
            Node(1.5, 0.5, "N5", False),
            Node(0, -0.5, "N6", False), #5
            Node(1, -0.5, "N7", False), #6
            Node(0, 1.5, "N8", False), #7
            Node(1, 1.5, "N9", False), #8
            Node(1.5, 0, "N10", False), #9
        ]

        for n in nodes:
            g.add_node(n)

        # Create edges
        edges = [
            (nodes[0], nodes[1]),
            (nodes[1], nodes[4]),
            (nodes[2], nodes[4]),
            (nodes[3], nodes[2]),
            (nodes[0], nodes[3]),
            (nodes[0], nodes[5]),
            (nodes[1], nodes[6]),
            (nodes[5], nodes[6]),
            (nodes[3], nodes[7]),
            (nodes[2], nodes[8]),
            (nodes[7], nodes[8]),
            (nodes[1], nodes[9]),
            (nodes[4], nodes[9]),
            (nodes[6], nodes[9]),
        ]

        for u, v in edges:
            g.add_edge(HyperEdge((u, v), "E"))

        # Create the hyperedge for the production
        hyperedge = HyperEdge((nodes[0], nodes[1], nodes[2], nodes[3], nodes[4]), "P", r=True)
        g.add_hyper_edge(hyperedge)

        draw(g)
        P9().apply(g)
        draw(g)

    @staticmethod
    def case4():
        g = Graph()

        # Create nodes
        nodes = [
            Node(0, 0, "N1", False),
            Node(1, 0, "N2", False),
            Node(1, 1, "N3", False),
            Node(0, 1, "N4", False),
            Node(1.5, 0.5, "N5", False),
            Node(0, -0.5, "N6", False), #5
            Node(1, -0.5, "N7", False), #6
            Node(0, 1.5, "N8", False), #7
            Node(1, 1.5, "N9", False), #8
            Node(1.5, 0, "N10", False), #9
        ]

        for n in nodes:
            g.add_node(n)

        # Create edges
        edges = [
            (nodes[0], nodes[1], False),
            (nodes[1], nodes[4], False),
            (nodes[2], nodes[4], True),
            (nodes[3], nodes[2], False),
            (nodes[0], nodes[3], False),
            (nodes[0], nodes[5], False),
            (nodes[1], nodes[6], False),
            (nodes[5], nodes[6], False),
            (nodes[3], nodes[7], False),
            (nodes[2], nodes[8], False),
            (nodes[7], nodes[8], False),
            (nodes[1], nodes[9], False),
            (nodes[4], nodes[9], False),
            (nodes[6], nodes[9], False),
        ]

        for u, v, b in edges:
            g.add_edge(HyperEdge((u, v), "E", b=b))

        # Create the hyperedge for the production
        hyperedge = HyperEdge((nodes[0], nodes[1], nodes[2], nodes[3], nodes[4]), "P", r=True)
        g.add_hyper_edge(hyperedge)

        draw(g)
        P9().apply(g)
        draw(g)

    @staticmethod
    def case5():
        g = Graph()

        # Create nodes
        nodes = [
            Node(0, 0, "N1", False),
            Node(1, 0, "N2", False),
            Node(1, 1, "N3", False),
            Node(0, 1, "N4", False),
            Node(1.5, 0.5, "N5", False),
            Node(0, -0.5, "N6", False), #5
            Node(1, -0.5, "N7", False), #6
            Node(0, 1.5, "N8", False), #7
            Node(1, 1.5, "N9", False), #8
            Node(1.5, 0, "N10", False), #9
        ]

        for n in nodes:
            g.add_node(n)

        # Create edges
        edges = [
            (nodes[0], nodes[1]),
            (nodes[1], nodes[4]),

            (nodes[3], nodes[2]),
            (nodes[0], nodes[3]),
            (nodes[0], nodes[5]),
            (nodes[1], nodes[6]),
            (nodes[5], nodes[6]),
            (nodes[3], nodes[7]),
            (nodes[2], nodes[8]),
            (nodes[7], nodes[8]),
            (nodes[1], nodes[9]),
            (nodes[4], nodes[9]),
            (nodes[6], nodes[9]),
        ]

        for u, v in edges:
            g.add_edge(HyperEdge((u, v), "E"))

        # Create the hyperedge for the production
        hyperedge = HyperEdge((nodes[0], nodes[1], nodes[2], nodes[3], nodes[4]), "P", r=True)
        g.add_hyper_edge(hyperedge)

        draw(g)
        P9().apply(g)
        draw(g)
