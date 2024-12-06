from structure.graph import Graph
from util.iso import find_isomorphisms


class Production:

    def apply(self, graph: Graph):
        for iso_map in find_isomorphisms(graph.get(), self.left_side().get()):
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
            right: Graph = self.right_side(left)
            for node in right.get_nodes():
                graph.add_node(node)
            for u, v in right.get_edges():
                graph._G.add_edge(u, v)

    @staticmethod
    def left_side():
        raise NotImplementedError

    @staticmethod
    def right_side(left):
        raise NotImplementedError
