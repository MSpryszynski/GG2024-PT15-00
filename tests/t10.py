from plotting.plot import draw
from productions.p10 import P10
from structure.graph import Graph
from structure.hyperedge import HyperEdge
from structure.node import Node
from tests.test import Test

class T10(Test):
    @staticmethod
    def run():
        T10.case1()
        T10.case2()
        T10.case3()
        T10.case4()
        T10.case5()

    @staticmethod
    def case1():
        g = Graph()

        # Create nodes
        nodes = [
            Node(0, 0, "N1"),
            Node(1, 0, "N2"),
            Node(1, 1, "N3"),
            Node(0, 1, "N4"),
            Node(1.5, 0.5, "N5"),
            Node(0.5, 0, "N6", h = True)
        ]

        for n in nodes:
            g.add_node(n)

        # Create edges
        edges = [
            (nodes[0], nodes[5]),  # n1 - n6
            (nodes[5], nodes[1]),  # n6 - n2
            (nodes[1], nodes[4]),  # n2 - n5
            (nodes[2], nodes[4]),  # n3 - n5
            (nodes[3], nodes[2]),  # n4 - n3
            (nodes[0], nodes[3]),  # n4 - n1
        ]

        for u, v in edges:
            g.add_edge(HyperEdge((u, v), "E"))

        # Create the hyperedge for the production
        hyperedge = HyperEdge((nodes[0], nodes[1], nodes[2], nodes[3], nodes[4]), "P", r=True)
        g.add_hyper_edge(hyperedge)

        draw(g)
        P10().apply(g)
        draw(g)

    @staticmethod
    def case2():
        g = Graph()

        # Create nodes
        nodes = [
            Node(0, 0, "N1"),
            Node(1, 0, "N2"),
            Node(1, 1, "N3"),
            Node(0, 1, "N4"),
            Node(1.5, 0.5, "N5"),
            Node(0.5, 0, "N6", h = True)
        ]

        for n in nodes:
            g.add_node(n)

        # Create edges
        edges = [
            (nodes[0], nodes[5]),  # n1 - n6
            (nodes[5], nodes[1]),  # n6 - n2
            (nodes[1], nodes[4]),  # n2 - n5
            (nodes[2], nodes[4]),  # n3 - n5
            (nodes[3], nodes[2]),  # n4 - n3
            (nodes[0], nodes[3]),  # n4 - n1
        ]

        for u, v in edges:
            g.add_edge(HyperEdge((u, v), "E"))

        # Create the hyperedge for the production
        hyperedge = HyperEdge((nodes[0], nodes[1], nodes[2], nodes[3], nodes[4]), "P", r=False)
        g.add_hyper_edge(hyperedge)

        draw(g)
        P10().apply(g)
        draw(g)

    @staticmethod
    def case3():
        g = Graph()

        # Create nodes
        nodes = [
            Node(0, 0, "N1"), #0
            Node(1, 0, "N2"), #1
            Node(1, 1, "N3"), #2
            Node(0, 1, "N4"), #3
            Node(1.5, 0.5, "N5"), #4
            Node(0.5, 0, "N6", h = True), #5
            Node(0, -0.5, "N7", False), #6
            Node(1, -0.5, "N8", False), #7
            Node(0, 1.5, "N9", False), #8
            Node(1, 1.5, "N10", False), #9
            Node(1.5, 0, "N11", False), #10
        ]

        for n in nodes:
            g.add_node(n)

        edges = [
            (nodes[0], nodes[5]),  # n1 - n6
            (nodes[5], nodes[1]),  # n6 - n2
            (nodes[1], nodes[4]),  # n2 - n5
            (nodes[2], nodes[4]),  # n3 - n5
            (nodes[3], nodes[2]),  # n4 - n3
            (nodes[0], nodes[3]),  # n4 - n1
            (nodes[0], nodes[6]),
            (nodes[1], nodes[7]),
            (nodes[6], nodes[7]),
            (nodes[3], nodes[8]),
            (nodes[2], nodes[9]),
            (nodes[8], nodes[9]),
            (nodes[1], nodes[10]),
            (nodes[4], nodes[10]),
            (nodes[7], nodes[10])
        ]

        for u, v in edges:
            g.add_edge(HyperEdge((u, v), "E"))

        # Create the hyperedge for the production
        hyperedge = HyperEdge((nodes[0], nodes[1], nodes[2], nodes[3], nodes[4]), "P", r=True)
        g.add_hyper_edge(hyperedge)

        draw(g)
        P10().apply(g)
        draw(g)

    @staticmethod
    def case4():
        g = Graph()

        # Create nodes
        nodes = [
            Node(0, 0, "N1"), #0
            Node(1, 0, "N2"), #1
            Node(1, 1, "N3"), #2
            Node(0, 1, "N4"), #3
            Node(1.5, 0.5, "N5"), #4
            Node(0.5, 0, "N6", h = True), #5
            Node(0, -0.5, "N7", False), #6
            Node(1, -0.5, "N8", False), #7
            Node(0, 1.5, "N9", False), #8
            Node(1, 1.5, "N10", False), #9
            Node(1.5, 0, "N11", False), #10
        ]

        for n in nodes:
            g.add_node(n)

        edges = [
            (nodes[0], nodes[5], False),  # n1 - n6
            (nodes[5], nodes[1], False),  # n6 - n2
            (nodes[1], nodes[4], False),  # n2 - n5
            (nodes[2], nodes[4], True),  # n3 - n5
            (nodes[3], nodes[2], False),  # n4 - n3
            (nodes[0], nodes[3], False),  # n4 - n1
            (nodes[0], nodes[6], False),
            (nodes[1], nodes[7], False),
            (nodes[6], nodes[7], False),
            (nodes[3], nodes[8], False),
            (nodes[2], nodes[9], False),
            (nodes[8], nodes[9], False),
            (nodes[1], nodes[10], False),
            (nodes[4], nodes[10], False),
            (nodes[7], nodes[10], False)
        ]

        for u, v, b in edges:
            g.add_edge(HyperEdge((u, v), "E", b=b))

        # Create the hyperedge for the production
        hyperedge = HyperEdge((nodes[0], nodes[1], nodes[2], nodes[3], nodes[4]), "P", r=True)
        g.add_hyper_edge(hyperedge)

        draw(g)
        P10().apply(g)
        draw(g)

    @staticmethod
    def case5():
        g = Graph()

        # Create nodes
        nodes = [
            Node(0, 0, "N1"), #0
            Node(1, 0, "N2"), #1
            Node(1, 1, "N3"), #2
            Node(0, 1, "N4"), #3
            Node(1.5, 0.5, "N5"), #4
            Node(0.5, 0, "N6", h = True), #5
            Node(0, -0.5, "N7", False), #6
            Node(1, -0.5, "N8", False), #7
            Node(0, 1.5, "N9", False), #8
            Node(1, 1.5, "N10", False), #9
            Node(1.5, 0, "N11", False), #10
        ]

        for n in nodes:
            g.add_node(n)

        edges = [
            (nodes[0], nodes[5]),  # n1 - n6
            (nodes[5], nodes[1]),  # n6 - n2
            (nodes[1], nodes[4]),  # n2 - n5

            (nodes[3], nodes[2]),  # n4 - n3
            (nodes[0], nodes[3]),  # n4 - n1
            (nodes[0], nodes[6]),
            (nodes[1], nodes[7]),
            (nodes[6], nodes[7]),
            (nodes[3], nodes[8]),
            (nodes[2], nodes[9]),
            (nodes[8], nodes[9]),
            (nodes[1], nodes[10]),
            (nodes[4], nodes[10]),
            (nodes[7], nodes[10])
        ]

        for u, v in edges:
            g.add_edge(HyperEdge((u, v), "E"))

        # Create the hyperedge for the production
        hyperedge = HyperEdge((nodes[0], nodes[1], nodes[2], nodes[3], nodes[4]), "P", r=True)
        g.add_hyper_edge(hyperedge)

        draw(g)
        P10().apply(g)
        draw(g)
