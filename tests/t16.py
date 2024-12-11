from plotting.plot import draw
from productions.p10 import P10
from productions.p16 import P16
from structure.graph import Graph
from structure.hyperedge import HyperEdge
from structure.node import Node
from tests.test import Test

class T16(Test):
    @staticmethod
    def run():
        # Test Case 1: Production can be applied
        T16.case1()

        # Test Case 2: Production cannot be applied (e.g., r=False)
        # T16.case2()

    @staticmethod
    def case1():
        g = Graph()

        # Create nodes
        nodes = [
            Node(1, 0, "N1"),
            Node(4, 0, "N2"),
            Node(4, 3, "N3"),
            Node(1, 3, "N4"),
            Node(0, 1.5, "N5")
        ]

        for n in nodes:
            g.add_node(n)

        # Create the hyperedge for the production
        hyperedge = HyperEdge((nodes[0], nodes[1], nodes[2], nodes[3], nodes[4]), "P", r=False)
        g.add_hyper_edge(hyperedge)

        draw(g)
        P16().apply(g)
        draw(g)

    @staticmethod
    def case2():
        g = Graph()

        # Create nodes
        nodes = [
            Node(1, 0, "N1"),
            Node(4, 0, "N2"),
            Node(4, 3, "N3"),
            Node(1, 3, "N4"),
            Node(0, 1.5, "N5")
        ]

        for n in nodes:
            g.add_node(n)

        # Create the hyperedge for the production
        hyperedge = HyperEdge((nodes[0], nodes[1], nodes[2], nodes[3], nodes[4]), "P", r=True)
        g.add_hyper_edge(hyperedge)

        draw(g)
        P16().apply(g)
        draw(g)
