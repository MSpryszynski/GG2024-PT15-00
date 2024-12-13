from plotting.plot import draw
from productions.p10 import P10
from structure.graph import Graph
from structure.hyperedge import HyperEdge
from structure.node import Node
from tests.test import Test

class T10(Test):
    @staticmethod
    def run():
        # Test Case 1: Production can be applied
        T10.case1()

        # Test Case 2: Production cannot be applied (e.g., r=False)
        T10.case2()

        T10.case3()

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
            Node(0, 0, "N1"),
            Node(1, 0, "N2"),
            Node(1, 1, "N3"),
            Node(0, 1, "N4"),
            Node(1.5, 0.5, "N5"),
            Node(0.5, 0, "N6", h = False)
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
