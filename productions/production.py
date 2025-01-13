from structure.graph import Graph
from structure.hyperedge import HyperEdge
from util.iso import find_isomorphisms


def get_boundary(boundary_map, u, v):
    try:
        return boundary_map[(u, v)]["boundary"]
    except KeyError:
        return boundary_map[(v, u)]["boundary"]


def get_boundary_map(graph: Graph):
    boundary_map = {}
    for u, v in graph.get_edges():
        data = graph.get().get_edge_data(u, v)
        boundary_map[(u, v)] = data
    return boundary_map


class Production:

    def apply(self, graph: Graph):
        boundary_map = get_boundary_map(graph)
        iso_map = find_isomorphisms(graph.get(), self.left_side().get())
        left: Graph = self.left_side()
        ordered_nodes_update = {}
        for v_self, v_left in iso_map.items():
            i = left.ordered_nodes.index(v_left)
            ordered_nodes_update[i] = v_self
        for u, v in left.get_edges():
            v = left.ordered_nodes.index(v)
            u = left.ordered_nodes.index(u)
            graph.remove_edge(ordered_nodes_update[u], ordered_nodes_update[v])
        for node in left.get_nodes():
            if node.hyper:
                graph.remove_node(ordered_nodes_update[left.ordered_nodes.index(node)])
        for i, node in ordered_nodes_update.items():
            left.ordered_nodes[i] = node
        right: Graph = self.right_side(left.ordered_nodes, boundary_map)
        for node in right.get_nodes():
            graph.add_node(node)
        for u, v in right.get_edges():
            edge_data = right.get().get_edge_data(u, v)
            graph.add_edge(HyperEdge({u, v}, "E", edge_data["boundary"]))

    @staticmethod
    def left_side():
        raise NotImplementedError

    @staticmethod
    def right_side(iso_ordered_nodes, boundary_map):
        raise NotImplementedError
