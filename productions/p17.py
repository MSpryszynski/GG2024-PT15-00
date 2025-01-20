from productions.production import Production
from structure.graph import Graph
from structure.hyperedge import HyperEdge
from structure.node import Node
from util.calculations import get_middle_node_coords


class P17(Production):
    @staticmethod
    def left_side() -> Graph:
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

        return g

    @staticmethod
    def right_side(iso_ordered_nodes, boundary_map) -> Graph:
        n1, n2, n3, n4, n5, n6, n7, n8, q1, q2 = iso_ordered_nodes

        g = Graph()
        for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
            g.add_node(n)

        e1 = HyperEdge((n2, n5), 'E', False, False)
        e2 = HyperEdge((n5, n3), 'E', False, False)
        e3 = HyperEdge((n1, n2, n3, n4, n8), 'Q', False, True)
        e4 = HyperEdge((n3, n5, n6, n7), 'Q', False, True)

        for e in [e1, e2]:
            g.add_edge(e)

        for e in [e3, e4]:
            g.add_hyper_edge(e)

        return g
