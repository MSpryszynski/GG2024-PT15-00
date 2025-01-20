from productions.production import Production
from structure.graph import Graph
from structure.hyperedge import HyperEdge
from structure.node import Node
from util.calculations import get_middle_node_coords


class P11(Production):
    @staticmethod
    def left_side() -> Graph:
        g = Graph()
        n1 = Node(0, 0, "N1", False)
        n2 = Node(1, 0, "N2", False)
        n3 = Node(1, 1, "N3", False)
        n4 = Node(0, 1, "N4", False)
        n5 = Node(1.5, 0.5, "N5", False)

        x6, y6 = get_middle_node_coords([n1, n2])
        n6 = Node(x6, y6, "N6", True)
        x7, y7 = get_middle_node_coords([n1, n4])
        n7 = Node(x7, y7, "N7", True)

        for n in [n1, n2, n3, n4, n5, n6, n7]:
            g.add_node(n)

        e1 = HyperEdge((n1, n6), 'E', False, False)
        e2 = HyperEdge((n6, n2), 'E', False, False)
        e3 = HyperEdge((n2, n5), 'E', False, False)
        e4 = HyperEdge((n5, n3), 'E', False, False)
        e5 = HyperEdge((n3, n4), 'E', False, False)
        e6 = HyperEdge((n4, n7), 'E', False, False)
        e7 = HyperEdge((n7, n1), 'E', False, False)
        e8 = HyperEdge((n1, n2, n3, n4, n5), 'Q', False, True)

        g.add_edge(e1)
        g.add_edge(e2)
        g.add_edge(e3)
        g.add_edge(e4)
        g.add_edge(e5)
        g.add_edge(e6)
        g.add_edge(e7)
        g.add_hyper_edge(e8)

        return g

    @staticmethod
    def right_side(iso_ordered_nodes, boundary_map) -> Graph:
        n1, n2, n3, n4, n5, n6, n7, q = iso_ordered_nodes
        # n1, n2, n3, n4, n5, n6, n7, q, hn1, hn2, hn3, hn4, hn5, hn6, hn7, hn8 = left.ordered_nodes

        g = Graph()
        print(n7)
        # x6, y6 = get_middle_node_coords([n1, n2])
        # x7, y7 = get_middle_node_coords([n1, n4])
        x8, y8 = get_middle_node_coords([n3, n4])  # upper
        x9, y9 = get_middle_node_coords([n3, n5])  # right upper
        x10, y10 = get_middle_node_coords([n2, n5])  # right lower
        x11, y11 = get_middle_node_coords([n1, n2, n3, n4, n5])  # center node

        n6.h = False
        n7.h = False
        n8 = Node(x8, y8, "N8", not boundary_map[(n3, n4)]["boundary"])
        n9 = Node(x9, y9, "N9", not boundary_map[(n3, n5)]["boundary"])
        n10 = Node(x10, y10, "N10", not boundary_map[(n2, n5)]["boundary"])
        n11 = Node(x11, y11, "N11", False)
        # n6 = Node(x6, y6, "N6", False)
        # n7 = Node(x7, y7, "N7", False)
        # n8 = Node(x8, y8, "N8", False)
        # n9 = Node(x9, y9, "N9", False)
        # n10 = Node(x10, y10, "N10", False)
        # n11 = Node(x11, y11, "N11", False)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11]:
            g.add_node(n)

        # around
        e1 = HyperEdge((n1, n6), 'E', boundary_map[(n1, n6)]["boundary"])
        e2 = HyperEdge((n6, n2), 'E', boundary_map[(n2, n6)]["boundary"])
        e3 = HyperEdge((n2, n10), 'E', boundary_map[(n2, n5)]["boundary"])
        e4 = HyperEdge((n10, n5), 'E', boundary_map[(n2, n5)]["boundary"])
        e5 = HyperEdge((n5, n9), 'E', boundary_map[(n3, n5)]["boundary"])
        e6 = HyperEdge((n9, n3), 'E', boundary_map[(n3, n5)]["boundary"])
        e7 = HyperEdge((n3, n8), 'E', boundary_map[(n3, n4)]["boundary"])
        e8 = HyperEdge((n8, n4), 'E', boundary_map[(n3, n4)]["boundary"])
        e9 = HyperEdge((n4, n7), 'E', boundary_map[(n4, n7)]["boundary"])
        e10 = HyperEdge((n7, n1), 'E', boundary_map[(n4, n7)]["boundary"])

        # e1 = HyperEdge((n1, n6), 'E', False, False)
        # e2 = HyperEdge((n6, n2), 'E', False, False)
        # e3 = HyperEdge((n2, n10), 'E', False, False)
        # e4 = HyperEdge((n10, n5), 'E', False, False)
        # e5 = HyperEdge((n5, n9), 'E', False, False)
        # e6 = HyperEdge((n9, n3), 'E', False, False)
        # e7 = HyperEdge((n3, n8), 'E', False, False)
        # e8 = HyperEdge((n8, n4), 'E', False, False)
        # e9 = HyperEdge((n4, n7), 'E', False, False)
        # e10 = HyperEdge((n7, n1), 'E', False, False)

        # center
        e11 = HyperEdge((n6, n11), 'E', False, True)
        e12 = HyperEdge((n7, n11), 'E', False, True)
        e13 = HyperEdge((n8, n11), 'E', False, True)
        e14 = HyperEdge((n9, n11), 'E', False, True)
        e15 = HyperEdge((n10, n11), 'E', False, True)

        # inside Q tag
        e16 = HyperEdge((n1, n6, n11, n7), 'Q', False, False)
        e17 = HyperEdge((n6, n2, n10, n11), 'Q', False, False)
        e18 = HyperEdge((n10, n5, n9, n11), 'Q', False, False)
        e19 = HyperEdge((n9, n3, n8, n11), 'Q', False, False)
        e20 = HyperEdge((n8, n4, n7, n11), 'Q', False, False)
        for e in [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15]:
            g.add_edge(e)

        for e in [e16, e17, e18, e19, e20]:
            g.add_hyper_edge(e)

        return g
