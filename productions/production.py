from structure.graph import Graph
from structure.hyperedge import HyperEdge
from util.iso import find_isomorphisms


class Production:

    def apply(self, graph: Graph):
        for iso_map in find_isomorphisms(graph.get(), self.left_side().get()):
            left: Graph = self.left_side()
            ordered_nodes_update = {}
            for v_self, v_left in iso_map.items():
                i = left.ordered_nodes.index(v_left)
                ordered_nodes_update[i] = v_self
            left_edge_to_graph_edge = {}
            for u, v in left.get_edges():
                i = left.ordered_nodes.index(v)
                j = left.ordered_nodes.index(u)
                left_edge_to_graph_edge[(u.label, v.label)] = graph.get_edge(ordered_nodes_update[i], ordered_nodes_update[j])
                left_edge_to_graph_edge[(v.label, u.label)] = graph.get_edge(ordered_nodes_update[i], ordered_nodes_update[j])
                graph.remove_edge(ordered_nodes_update[i], ordered_nodes_update[j])
            for node in left.get_nodes():
                if node.hyper:
                    graph.remove_node(ordered_nodes_update[left.ordered_nodes.index(node)])
            for i, node in ordered_nodes_update.items():
                left.ordered_nodes[i] = node
            right: Graph = self.right_side(left, left_edge_to_graph_edge)
            for node in right.get_nodes():
                graph.add_node(node)
            for u, v in right.get_edges():
                he = right.get_edge(u, v)
                graph.add_edge(he)

    @staticmethod
    def left_side():
        raise NotImplementedError

    @staticmethod
    def right_side(left: Graph, left_edge_to_graph_edge: dict[(str, str), HyperEdge]):
        raise NotImplementedError
