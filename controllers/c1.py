from controllers.controller import Controller
from plotting.plot import draw
from structure.graph import Graph
from structure.hyperedge import HyperEdge
from structure.node import Node


class C1(Controller):
    @staticmethod
    def run():
        g = Graph()
        n1 = Node(0, 0, "N1")
        n2 = Node(0, 4, "N2")
        n3 = Node(4, 4, "N3")
        n4 = Node(4, 0, "N4")
        n5 = Node(1, 1, "N5")
        n6 = Node(1, 3, "N6")
        n7 = Node(2, 3, "N7")
        n8 = Node(3, 2, "N8")
        n9 = Node(2, 1, "N9")
        n10 = Node(4, 2, "N10")

        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]:
            g.add_node(n)

        edges = [
            (n1, n2, False), (n2, n3, False), (n3, n10, False), (n10, n4, False),
            (n4, n1, False), (n1, n5, False), (n2, n6, False), (n3, n7, False),
            (n10, n8, False), (n9, n4, False), (n5, n6, False), (n6, n7, False),
            (n7, n8, False), (n8, n9, False), (n9, n5, False)
        ]

        for u, v, b_param in edges:
            g.add_edge(HyperEdge((u, v), "E", b_param))

        hyper_edges = [
            [(n1, n5, n6, n2), False], [(n2, n6, n7, n3), False],
            [(n7, n3, n10, n8), False], [(n8, n10, n4, n9), False],
            [(n4, n9, n5, n1), False], [(n5, n6, n7, n8, n9), False],
        ]

        for nodes, r in hyper_edges:
            if len(nodes) == 4:
                u, v, w, x = nodes
                g.add_hyper_edge(HyperEdge((u, v, w, x), "Q", r=r))
            else:
                u, v, w, x, y = nodes
                g.add_hyper_edge(HyperEdge((u, v, w, x, y), "Q", r=r))

        draw(g)
