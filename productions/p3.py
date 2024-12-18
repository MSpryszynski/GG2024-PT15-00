from structure.graph import Graph
from productions.production import Production
from structure.node import Node
from structure.hyperedge import HyperEdge


class P3(Production):
    @staticmethod
    def left_side() -> Graph:
        g = Graph()
        n1 = Node(1, 1, "N1")
        n2 = Node(2, 1, "N2")
        n3 = Node(2, 2, "N3")
        n4 = Node(1, 2, "N4")
        n5 = Node(2, 1.5, "N5", True)
        n6 = Node(1.5, 1, "N5", True)
        for n in [n1, n2, n3, n4, n5, n6]:
            g.add_node(n)

        edges = [
            (n1, n6), (n6, n2), (n2, n5), (n3, n4), (n4, n1), (n5, n3)
        ]
        for u, v in edges:
            g.add_edge(HyperEdge((u, v), "E"))
        e7 = HyperEdge((n1, n2, n3, n4), 'E', b=False, r=True)
        g.add_hyper_edge(e7)
        return g

    @staticmethod
    def right_side(iso_ordered_nodes, boundary_map):
        n1, n2, n3, n4, n5, n6, n7 = iso_ordered_nodes
        n5.h = False
        n6.h = False
        g = Graph()

        n7 = Node((n3.x + n4.x) / 2, (n3.y + n4.y) / 2, "N7", True)
        n8 = Node((n4.x + n1.x) / 2, (n4.y + n1.y) / 2, "N8", True)
        n9 = Node((n1.x + n2.x + n3.x + n4.x) / 4, (n1.y + n2.y + n3.y + n4.y) / 4, "N9", False)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9]:
            g.add_node(n)

        edges = [
            (n1, n6), (n6, n2), (n2, n5), (n5, n3),
            (n3, n7), (n7, n4), (n4, n8), (n8, n1),
            (n5, n9), (n6, n9), (n7, n9), (n8, n9),
        ]

        for u, v in edges:
            g.add_edge(HyperEdge((u, v), "E"))

        hyper_edges = [
            (n1, n8, n9, n6), (n5, n2, n6, n9),
            (n8, n9, n7, n4), (n9, n5, n3, n7)
        ]
        for u, v, w, x in hyper_edges:
            g.add_hyper_edge(HyperEdge((u, v, w, x), "Q"))

        return g
