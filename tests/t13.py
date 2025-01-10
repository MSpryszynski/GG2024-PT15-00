from plotting.plot import draw
from productions.p13 import P13
from structure.graph import Graph
from structure.hyperedge import HyperEdge
from structure.node import Node
from tests.test import Test
from util.calculations import get_middle_node_coords


class T13(Test):
    @staticmethod
    def run():
        T13.case_basic_production()
        T13.case_no_izomorphic()
        T13.case_invalid_h_value()
        T13.case_find_in_subgraph()
        T13.case_invalid_hyper_edge_label()
        
    @staticmethod
    def case_basic_production():
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
        e3 = HyperEdge((n5, n2), 'E', False, False)
        e4 = HyperEdge((n5, n3), 'E', True, False)
        e5 = HyperEdge((n8, n3), 'E', False, False)
        e6 = HyperEdge((n8, n4), 'E', False, False)
        e7 = HyperEdge((n4, n7), 'E', True, False)
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

        draw(g)
        P13().apply(g)
        draw(g)
    
    @staticmethod
    def case_no_izomorphic():
        g = Graph()
        nodes = [
            Node(0, 0, "N1", False),
            Node(1, 0, "N2", False),
            Node(1, 1, "N3", False),
            Node(0, 1, "N4", False),
            Node(1.5, 0.5, "N5", False)
        ]
        for node in nodes:
            g.add_node(node)
        
        edges = [
            (nodes[0], nodes[1]),   # N1-N2
            (nodes[1], nodes[4]),   # N2-N5
            (nodes[4], nodes[2]),   # N5-N3
            (nodes[2], nodes[3]),   # N3-N4
            (nodes[3], nodes[0]),   # N4-N1
            (nodes[1], nodes[2])    # N2-N3
        ]

        for edge in edges:
            g.add_edge(HyperEdge(edge, "E"))
        
        g.add_hyper_edge(HyperEdge(tuple(nodes[:-1]), 'E', False, True)) # do not connect N5 to hyperedge

        draw(g)
        P13().apply(g)
        draw(g)
    
    @staticmethod
    def case_invalid_h_value():
        g = Graph()
        n1 = Node(0, 0, "N1", False)
        n2 = Node(1, 0, "N2", False)
        n3 = Node(1, 1, "N3", False)
        n4 = Node(0, 1, "N4", False)
        n5 = Node(1.5, 0.5, "N5", False)

        x6, y6 = get_middle_node_coords([n1, n2])
        n6 = Node(x6, y6, "N6", False)  # {!} invalid h-value - should be true
        x7, y7 = get_middle_node_coords([n1, n4])
        n7 = Node(x7, y7, "N7", True)
        x8, y8 = get_middle_node_coords([n4, n3])
        n8 = Node(x8, y8, "N8", True)
        e1 = HyperEdge((n1, n6), 'E', False, False)
        e2 = HyperEdge((n6, n2), 'E', False, False)
        e3 = HyperEdge((n5, n2), 'E', False, False)
        e4 = HyperEdge((n5, n3), 'E', True, False)
        e5 = HyperEdge((n8, n3), 'E', False, False)
        e6 = HyperEdge((n8, n4), 'E', False, False)
        e7 = HyperEdge((n4, n7), 'E', True, False)
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

        draw(g)
        P13().apply(g)
        draw(g)

    @staticmethod
    def case_find_in_subgraph():
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
        e3 = HyperEdge((n5, n2), 'E', False, False)
        e4 = HyperEdge((n5, n3), 'E', True, False)
        e5 = HyperEdge((n8, n3), 'E', False, False)
        e6 = HyperEdge((n8, n4), 'E', False, False)
        e7 = HyperEdge((n4, n7), 'E', True, False)
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

        # extra nodes
        extra_nodes = [
            Node(1.5, 0, "NX0", False),
            Node(1.5, 1, "NX1", False),
            Node(0, 1.5, "NX2", False),
            Node(1, 1.5, "NX3", False),
            Node(0, -0.5, "NX4", False),
            Node(1, -0.5, "NX5", False),
            Node(1.5, -0.5, "NX6", False),
            Node(1.5, 1.5, "NX7", False)
        ]

        # extra edges
        extra_edges_data = [
            (n1, extra_nodes[4]),
            (extra_nodes[4], extra_nodes[5]),
            (extra_nodes[5], n2),
            (n2, extra_nodes[0]),
            (extra_nodes[0], n5),
            (n5, extra_nodes[1]),
            (extra_nodes[1], n3),
            (n3, extra_nodes[3]),
            (n4, extra_nodes[2]),
            (extra_nodes[2], extra_nodes[3]),
            (extra_nodes[5], extra_nodes[6]),
            (extra_nodes[6], extra_nodes[0]),
            (extra_nodes[1], extra_nodes[7]),
            (extra_nodes[7], extra_nodes[3])
        ]

        for n in extra_nodes:
            g.add_node(n)
        
        for e_data in extra_edges_data:
            g.add_hyper_edge(HyperEdge(e_data, 'E'))
        
        draw(g)
        P13().apply(g)
        draw(g)

    @staticmethod
    def case_invalid_hyper_edge_label():    # "Q" instead of "P"
        pass
    