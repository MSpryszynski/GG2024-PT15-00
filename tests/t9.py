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
        # Test Case 1: Production can be applied
        T9.case1()

        # Test Case 2: Production cannot be applied (e.g., r=False)
        # T9.case2()

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
