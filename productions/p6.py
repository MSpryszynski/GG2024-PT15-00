from productions.production import Production
from structure.graph import Graph
from structure.hyperedge import HyperEdge
from structure.node import Node
from util.calculations import get_middle_node_coords


class P6(Production):
    @staticmethod
    def left_side() -> Graph:
        g = Graph()
        n1 = Node(1, 1, "N1")
        n2 = Node(2, 1, "N2")
        n3 = Node(2, 2, "N3")
        n4 = Node(1, 2, "N4")
        x, y = get_middle_node_coords([n2, n3])
        n5 = Node(x, y, "N5", h=True)
        x, y = get_middle_node_coords([n1, n2])
        n6 = Node(x, y, "N6", h=True)
        x, y = get_middle_node_coords([n1, n4])
        n7 = Node(x, y, "N7", h=True)
        x, y = get_middle_node_coords([n3, n4])
        n8 = Node(x, y, "N8", h=True)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
            g.add_node(n)

        edges = [
            (n1, n6), (n6, n2), (n2, n5), (n5, n3),
            (n3, n8), (n8, n4), (n4, n7), (n7, n1)
        ]

        for u, v in edges:
            g.add_edge(HyperEdge((u, v), "E"))

        hyper_edge = HyperEdge((n1, n2, n3, n4), "Q", r=True)
        g.add_hyper_edge(hyper_edge)

        return g

    @staticmethod
    def right_side(left: Graph) -> Graph:
        n1, n2, n3, n4, n5, n6, n7, n8, q = left.ordered_nodes
        g = Graph()

        n5 = Node(n5.x, n5.y, "N5")
        n6 = Node(n6.x, n6.y, "N6")
        n7 = Node(n7.x, n7.y, "N7")
        n8 = Node(n8.x, n8.y, "N8")

        x, y = get_middle_node_coords([n1, n2, n3, n4])
        n9 = Node(x, y, "N9")

        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9]:
            g.add_node(n)

        # edges need changes because boundaries have to be set
        # everything what has B1, B2, B3 or B4 on the right side need to be changed
        edges = [
            (n1, n6), (n6, n2), (n2, n5), (n5, n3),
            (n3, n8), (n8, n4), (n4, n7), (n7, n1),
            (n5, n9), (n6, n9), (n7, n9), (n8, n9),
        ]

        for u, v in edges:
            g.add_edge(HyperEdge((u, v), "E"))

        hyper_edges = [
            (n1, n6, n9, n7), (n6, n2, n5, n9),
            (n9, n5, n3, n8), (n7, n9, n8, n4)
        ]

        for u, v, w, x in hyper_edges:
            g.add_hyper_edge(HyperEdge((u, v, w, x), "Q"))

        return g