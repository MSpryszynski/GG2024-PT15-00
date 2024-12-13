from structure.graph import Graph
from productions.production import Production
from structure.node import Node
from structure.hyperedge import HyperEdge

class P16(Production):

    @staticmethod
    def left_side() -> Graph:
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

        return g

    @staticmethod
    def right_side(left: Graph) -> Graph:
        n1, n2, n3, n4, n5, q = left.ordered_nodes

        g = Graph()

        # Create the hyperedge for the production
        hyperedge = HyperEdge((n1, n2, n3, n4, n5), "P", r=True)
        g.add_hyper_edge(hyperedge)

        return g
