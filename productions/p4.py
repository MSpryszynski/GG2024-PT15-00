from structure.graph import Graph
from productions.production import Production, get_boundary
from structure.node import Node
from structure.hyperedge import HyperEdge


class P4(Production):
    @staticmethod
    def left_side() -> Graph:
        g = Graph()
        n1 = Node(1, 1, "N1")
        n2 = Node(2, 1, "N2")
        n3 = Node(2, 2, "N3")
        n4 = Node(1, 2, "N4")
        n5 = Node(2, 1.5, "N5", True)
        n6 = Node(1, 1.5, "N6", True)
        for n in [n1, n2, n3, n4, n5, n6]:
            g.add_node(n)

        edges = [
            (n1, n6), (n6, n4), (n4, n3), (n3, n5), (n5, n2), (n1, n2)
        ]
        for u, v in edges:
            g.add_edge(HyperEdge((u, v), "E"))
        e7 = HyperEdge((n1, n2, n3, n4), 'Q', b=False, r=True)
        g.add_hyper_edge(e7)
        return g

    @staticmethod
    def right_side(iso_ordered_nodes, boundary_map):
        n1, n2, n3, n4, n5, n6, n7 = iso_ordered_nodes
        n5.h = False
        n6.h = False
        g = Graph()

        n7 = Node((n1.x + n2.x) / 2, (n1.y + n2.y) / 2, "N7", not get_boundary(boundary_map, n1, n2))
        n8 = Node((n3.x + n4.x) / 2, (n3.y + n4.y) / 2, "N8", not get_boundary(boundary_map, n3, n4))
        n9 = Node((n1.x + n2.x + n3.x + n4.x) / 4, (n1.y + n2.y + n3.y + n4.y) / 4, "N9", False)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9]:
            g.add_node(n)

        edges = [
            (n1, n6, get_boundary(boundary_map, n1, n6)),
            (n6, n4, get_boundary(boundary_map, n6, n4)),
            (n4, n8, get_boundary(boundary_map, n4, n3)),
            (n8, n3, get_boundary(boundary_map, n4, n3)),
            (n3, n5, get_boundary(boundary_map, n3, n5)),
            (n5, n2, get_boundary(boundary_map, n5, n2)),
            (n2, n7, get_boundary(boundary_map, n1, n2)),
            (n7, n1, get_boundary(boundary_map, n1, n2)),
            (n5, n9, False),
            (n6, n9, False),
            (n7, n9, False),
            (n8, n9, False),
        ]

        for u, v, boundary in edges:
            g.add_edge(HyperEdge((u, v), "E", boundary))

        hyper_edges = [
            (n1, n7, n9, n6), (n5, n2, n7, n9),
            (n8, n9, n3, n5), (n8, n9, n4, n6)
        ]
        for u, v, w, x in hyper_edges:
            g.add_hyper_edge(HyperEdge((u, v, w, x), "Q"))

        return g
