from structure.graph import Graph
from productions.production import Production
from structure.node import Node
from structure.edge import Edge


class P0(Production):
    @staticmethod
    def left_side() -> Graph:
        g = Graph()
        n1 = Node(1, 1, "N1")
        n2 = Node(2, 1, "N2")
        n3 = Node(2, 2, "N3")
        n4 = Node(1, 2, "N4")
        for n in [n1, n2, n3, n4]:
            g.add_node(n)

        edges = [
            (n1, n2), (n2, n3), (n3, n4), (n4, n1)
        ]
        for u, v in edges:
            g.add_edge(Edge((u, v), "E"))
        return g

    @staticmethod
    def right_side(left: Graph):
        n1, n2, n3, n4 = left.ordered_nodes
        g = Graph()

        n5 = Node((n1.x + n2.x) / 2, (n1.y + n2.y) / 2, "N5")
        n6 = Node((n2.x + n3.x) / 2, (n2.y + n3.y) / 2, "N6")
        n7 = Node((n3.x + n4.x) / 2, (n3.y + n4.y) / 2, "N7")
        n8 = Node((n4.x + n1.x) / 2, (n4.y + n1.y) / 2, "N8")

        for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
            g.add_node(n)

        edges = [
            (n1, n5), (n5, n2), (n2, n6), (n6, n3),
            (n3, n7), (n7, n4), (n4, n8), (n8, n1)
        ]

        for u, v in edges:
            g.add_edge(Edge((u, v), "E"))

        return g
