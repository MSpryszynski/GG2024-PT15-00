from structure.graph import Graph
from productions.production import Production
from structure.node import Node
from structure.hyperedge import HyperEdge

from util.calculations import get_middle_node_coords

class P9(Production):

    @staticmethod
    def left_side() -> Graph:
        g = Graph()

        # Create nodes
        nodes = [
            Node(0, 0, "N1"),
            Node(1, 0, "N2"),
            Node(1, 1, "N3"),
            Node(0, 1, "N4"),
            Node(1.5, 0.5, "N5")
        ]

        for n in nodes:
            g.add_node(n)

        # Create edges
        edges = [
            (nodes[0], nodes[1]),  # n1 - n2
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

        return g

    @staticmethod
    def right_side(left: Graph) -> Graph:
        n1, n2, n3, n4, n5, q = left.ordered_nodes

        g = Graph()

        x6, y6 = get_middle_node_coords([n1, n2])
        x7, y7 = get_middle_node_coords([n2, n5])
        x8, y8 = get_middle_node_coords([n5, n3])
        x9, y9 = get_middle_node_coords([n3, n4])
        x10, y10 = get_middle_node_coords([n4, n1])
        x11, y11 = get_middle_node_coords([n1, n2, n5, n3, n4])

        # Create new nodes
        new_nodes = [
            Node(x6, y6, "N6"),
            Node(x7, y7, "N7"),
            Node(x8, y8, "N8"),
            Node(x9, y9, "N9"),
            Node(x10, y10, "N10"),
            Node(x11, y11, "N11", h = False)
        ]

        for n in new_nodes:
            g.add_node(n)

        # edges need changes because boundaries have to be set
        # everything what has B1, B2, B3, B4 or B5 on the right side need to be changed
        # Create edges
        out_edges = [
            (n1, new_nodes[0]),
            (new_nodes[0], n2),
            (n2, new_nodes[1]),
            (new_nodes[1], n5),
            (n5, new_nodes[2]),
            (new_nodes[2], n3),
            (n3, new_nodes[3]),
            (new_nodes[3], n4),
            (n4, new_nodes[4]),
            (new_nodes[4], n1)
        ]

        for u, v in out_edges:
            g.add_edge(HyperEdge((u, v), "E"))

        in_edges = [
            (new_nodes[-1], new_nodes[0]),  # n11 - n6
            (new_nodes[-1], new_nodes[1]),  # n11 - n7
            (new_nodes[-1], new_nodes[2]),  # n11 - n8
            (new_nodes[-1], new_nodes[3]),  # n11 - n9
            (new_nodes[-1], new_nodes[4]),  # n11 - n10
        ]

        for u, v in in_edges:
            g.add_edge(HyperEdge((u, v), "E", b = False))

        # Create hyperedges (Q-tag)
        hyperedges = [
            (n1, new_nodes[0], new_nodes[4], new_nodes[-1]),
            (n2, new_nodes[0], new_nodes[1], new_nodes[-1]),
            (n5, new_nodes[1], new_nodes[2], new_nodes[-1]),
            (n3, new_nodes[2], new_nodes[3], new_nodes[-1]),
            (n4, new_nodes[3], new_nodes[4], new_nodes[-1]),
        ]

        for u, v, w, x in hyperedges:
            g.add_hyper_edge(HyperEdge((u, v, w, x), "Q", r = False))

        return g
