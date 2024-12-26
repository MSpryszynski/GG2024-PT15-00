from productions.production import Production
from structure.graph import Graph
from structure.hyperedge import HyperEdge
from structure.node import Node
from util.calculations import get_middle_node_coords


class P8(Production):
    @staticmethod
    def left_side() -> Graph:
        g = Graph()
        n1 = Node(1, 1, "N1", h=None)
        n2 = Node(2, 1, "N2", h=None)
        n3 = Node(2, 2, "N3", h=None)
        n4 = Node(1, 2, "N4", h=None)
        x, y = get_middle_node_coords([n2, n3])
        n5 = Node(x, y, "N5", h=True)
        n6 = Node(3, 1.5, "N6", h=None)
        n7 = Node(3, 2, "N7", h=None)

        for n in [n1, n2, n3, n4, n5, n6, n7]:
            g.add_node(n)

        edges = [
            (n2, n5), (n5, n3)
        ]

        for u, v in edges:
            g.add_edge(HyperEdge((u, v), "E"))

        hyper_edges = [
            [(n1, n2, n3, n4), False], [(n5, n6, n7, n3), True]
        ]

        for nodes, r in hyper_edges:
            u, v, w, x = nodes
            g.add_hyper_edge(HyperEdge((u, v, w, x), "Q", r=r))

        return g

    @staticmethod
    def right_side(iso_ordered_nodes, boundary_map) -> Graph:
        n1, n2, n3, n4, n5, n6, n7, q1, q2 = iso_ordered_nodes
        g = Graph()

        for n in [n1, n2, n3, n4, n5, n6, n7]:
            g.add_node(n)

        edges = [
            (n2, n5, boundary_map[(n2, n5)]["boundary"]),
            (n5, n3, boundary_map[(n3, n5)]["boundary"])
        ]

        for u, v, b_param in edges:
            g.add_edge(HyperEdge((u, v), "E", b=b_param))

        hyper_edges = [
            (n1, n2, n3, n4), (n5, n6, n7, n3)
        ]

        for u, v, w, x in hyper_edges:
            g.add_hyper_edge(HyperEdge((u, v, w, x), "Q", r=True))

        return g