from productions.production import Production
from structure.graph import Graph
from structure.hyperedge import HyperEdge
from structure.node import Node
from util.calculations import get_middle_node_coords


class P13(Production):
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
        x8, y8 = get_middle_node_coords([n4, n3])
        n8 = Node(x8, y8, "N8", True)
        e1 = HyperEdge((n1, n6), 'E', False, False)
        e2 = HyperEdge((n6, n2), 'E', False, False)
        e3 = HyperEdge((n2, n5), 'E', False, False)
        e4 = HyperEdge((n5, n3), 'E', False, False)
        e5 = HyperEdge((n8, n3), 'E', False, False)
        e6 = HyperEdge((n8, n4), 'E', False, False)
        e7 = HyperEdge((n4, n7), 'E', False, False)
        e8 = HyperEdge((n1, n7), 'E', False, False)
        e9 = HyperEdge((n1, n2, n3, n4, n5), 'E', False, True)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
            g.add_node(n)

        g.add_edge(e1)
        g.add_edge(e2)
        g.add_edge(e3)
        g.add_edge(e4)
        g.add_edge(e5)
        g.add_edge(e6)
        g.add_edge(e7)
        g.add_edge(e8)
        g.add_hyper_edge(e9, "P")


        return g

    @staticmethod
    def right_side(iso_ordered_nodes, boundary_map) -> Graph:
        n1, n2, n3, n4, n5, n6, n7, n8, q = iso_ordered_nodes
        g = Graph()

        n6.h = False
        n7.h = False
        n8.h = False

        for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
            g.add_node(n)
        
        # nc, aka node center, we are discarding exisitng q hyperedge
        nc = Node(q.x, q.y, "V", False)

        # nfu, aka node front upper
        xnfu, ynfu = get_middle_node_coords([n3,n5])
        nfu = Node(xnfu, ynfu, "V", not boundary_map[(n3, n5)]["boundary"])

        # nfl, aka node front lower
        xnfl, ynfl = get_middle_node_coords([n5,n2])
        nfl = Node(xnfl, ynfl, "V", not boundary_map[(n2, n5)]["boundary"])
        g.add_node(nfu)
        g.add_node(nfl)

        outer_edges = [
            (n1, n6, boundary_map[(n1, n6)]["boundary"]),
            (n6, n2, boundary_map[(n2, n6)]["boundary"]),
            (n2, nfl, boundary_map[(n2, n5)]["boundary"]), 
            (nfl, n5, boundary_map[(n2, n5)]["boundary"]), 
            (n5, nfu, boundary_map[(n3, n5)]["boundary"]), 
            (nfu, n3, boundary_map[(n3, n5)]["boundary"]), 
            (n3, n8, boundary_map[(n3, n8)]["boundary"]), 
            (n8, n4, boundary_map[(n4, n8)]["boundary"]), 
            (n4, n7, boundary_map[(n4, n7)]["boundary"]), 
            (n7, n1, boundary_map[(n1, n7)]["boundary"])
        ]

        for u, v, b in outer_edges:
            g.add_edge(HyperEdge((u, v), "E", b))

        hyper_edges = [
            (n1, n6, nc, n7), (n6, n2, nfl, nc), (nc, nfl, n5, nfu), (nc, nfu, n3, n8), (n7, nc, n8, n4)
        ]

        for u, v, w, x in hyper_edges:
            g.add_hyper_edge(HyperEdge((u, v, w, x), "Q", r=False))

        center_edges = [
            (n7, nc, True), (n6, nc, True), (nfl, nc, True), (nfu, nc, True), (n8, nc, True)
        ]

        for u, v, b in center_edges:
            g.add_edge(HyperEdge((u, v), "E", b))

        return g