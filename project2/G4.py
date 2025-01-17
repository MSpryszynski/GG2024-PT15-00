from plotting.plot import draw
from productions.p1 import P1
from productions.p2 import P2
from productions.p7 import P7
from productions.p8 import P8
from structure.graph import Graph
from structure.hyperedge import HyperEdge
from structure.node import Node

def selectorFn1(iso):
    max_x, max_y = 0, 0
    for iso_dict in iso:
        for main_graph_node, production_node in iso_dict.items():
            max_x, max_y = max(max_x, main_graph_node.x), max(max_y, main_graph_node.y)

    is_first, is_second = False, False
    for iso_dict in iso:
        for main_graph_node, production_node in iso_dict.items():
            if main_graph_node.x == max_x and main_graph_node.y == max_y:
                is_first = True
            if main_graph_node.x == max_x and main_graph_node.y != max_y:
                is_second = True
        if is_first and is_second:
            return iso_dict
        is_first, is_second = False, False

    raise Exception("Z wyrazami szacunu")

def selectorFn2(iso):
    max_x, max_y = 0, 0
    for iso_dict in iso:
        for main_graph_node, production_node in iso_dict.items():
            max_x, max_y = max(max_x, main_graph_node.x), max(max_y, main_graph_node.y)

    is_first, is_second = False, False
    for iso_dict in iso:
        for main_graph_node, production_node in iso_dict.items():
            if main_graph_node.x == max_x and main_graph_node.y == max_y:
                is_first = True
            if main_graph_node.y == max_y and main_graph_node.x != max_x:
                is_second = True
        if is_first and is_second:
            return iso_dict
        is_first, is_second = False, False

    raise Exception("Z wyrazami szacunu")

class G4:
    @staticmethod
    def run():
        g = Graph(is_main=True)

        def create_node(x, y):
            node = Node(x, y, None, False)
            return node

        n1 = create_node(0, 0)
        n2 = create_node(12, 0)
        n3 = create_node(12, 12)
        n4 = create_node(0, 12)
        n5 = create_node(4, 3)
        n6 = create_node(8, 3)
        n7 = create_node(10, 6)
        n8 = create_node(8, 9)
        n9 = create_node(4, 9)
        n10 = create_node(12, 6)

        e1 = HyperEdge((n1, n2), 'E', True, False)
        e2 = HyperEdge((n1, n4), 'E', True, False)
        e3 = HyperEdge((n2, n10), 'E', True, False)
        e4 = HyperEdge((n4, n3), 'E', True, False)
        e5 = HyperEdge((n9, n5), 'E', False, False)
        e6 = HyperEdge((n5, n6), 'E', False, False)
        e7 = HyperEdge((n6, n7), 'E', False, False)
        e8 = HyperEdge((n7, n8), 'E', False, False)
        e9 = HyperEdge((n8, n9), 'E', False, False)
        e10 = HyperEdge((n10, n7), 'E', False, False)
        e12 = HyperEdge((n10, n3), 'E', True, False)
        e15 = HyperEdge((n4, n9), 'E', False, False)
        e16 = HyperEdge((n3, n8), 'E', False, False)
        e17 = HyperEdge((n2, n6), 'E', False, False)
        e18 = HyperEdge((n1, n5), 'E', False, False)

        e19 = HyperEdge((n1, n5, n9, n4), 'E', True, False)
        e20 = HyperEdge((n2, n6, n7, n10), 'E', True, False)
        e21 = HyperEdge((n4, n3, n8, n9), 'E', True, False)
        e22 = HyperEdge((n5, n6, n7, n8, n9), 'E', True, False)
        e24 = HyperEdge((n10, n7, n8, n3), 'E', True, False)
        e25 = HyperEdge((n1, n2, n6, n5), 'E', True, False)

        g.add_node(n1)
        g.add_node(n2)
        g.add_node(n3)
        g.add_node(n4)
        g.add_node(n5)
        g.add_node(n6)
        g.add_node(n7)
        g.add_node(n8)
        g.add_node(n9)
        g.add_node(n10)
        g.add_edge(e1)
        g.add_edge(e2)
        g.add_edge(e3)
        g.add_edge(e4)
        g.add_edge(e5)
        g.add_edge(e6)
        g.add_edge(e7)
        g.add_edge(e8)
        g.add_edge(e9)
        g.add_edge(e10)
        g.add_edge(e12)
        g.add_edge(e15)
        g.add_edge(e16)
        g.add_edge(e17)
        g.add_edge(e18)
        g.add_hyper_edge(e19)
        g.add_hyper_edge(e20)
        g.add_hyper_edge(e21)
        g.add_hyper_edge(e22)
        g.add_hyper_edge(e24)
        g.add_hyper_edge(e25)

        # draw(g)
        P7().apply(g, selectorFn1)
        # draw(g)
        P1().apply(g)
        # draw(g)
        P7().apply(g, selectorFn1)
        # draw(g)
        P8().apply(g, selectorFn2)
        # draw(g)
        P2().apply(g)
        # draw(g)
        P1().apply(g)
        # draw(g)
        P7().apply(g, selectorFn1)
        # draw(g)
        P8().apply(g, selectorFn2)
        # draw(g)
        P2().apply(g)
        # draw(g)
        P1().apply(g)
        draw(g)
