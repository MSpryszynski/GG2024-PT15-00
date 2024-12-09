from productions.production import Production
from structure.graph import Graph
from structure.hyperedge import HyperEdge
from structure.node import Node
from util.calculations import get_middle_node_coords


class P8(Production):
    @staticmethod
    def left_side() -> Graph:
        g = Graph()
        n1 = Node(1, 1, "N1")
        n2 = Node(2, 1, "N2")
        n3 = Node(2, 2, "N3")
        n4 = Node(1, 2, "N4")
        x, y = get_middle_node_coords([n2, n3])
        n5 = Node(x, y, "N5", h=True)
        n6 = Node(3, 1.5, "N6")
        n7 = Node(3, 2, "N7")

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
    def right_side(left: Graph) -> Graph:
        n1, n2, n3, n4, n5, n6, n7, q = left.ordered_nodes
        g = Graph()

        for n in [n1, n2, n3, n4, n5, n6, n7]:
            g.add_node(n)

        # edges need changes because boundaries have to be set
        # everything what has B2 on the right side need to be changed
        edges = [
            (n2, n5), (n5, n3)
        ]

        for u, v in edges:
            g.add_edge(HyperEdge((u, v), "E"))

        hyper_edges = [
            (n1, n2, n3, n4), (n5, n6, n7, n3)
        ]

        for u, v, w, x in hyper_edges:
            g.add_hyper_edge(HyperEdge((u, v, w, x), "Q", r=True))

        return g