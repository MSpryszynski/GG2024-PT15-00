from structure.graph import Graph
from structure.node import Node
from structure.edge import Edge
from plotting.plot import draw
from productions.p0 import P0


def example():
    g = Graph()
    n1 = Node(0, 0, "N1", False)
    n2 = Node(1, 0, "N2", False)
    n3 = Node(1, 1, "N3", False)
    n4 = Node(0, 1, "N4", False)
    n5 = Node(2, 0, "N5", False)
    e1 = Edge((n1, n2), 'E', False, False)
    e2 = Edge((n1, n4), 'E', False, False)
    e3 = Edge((n2, n3), 'E', False, False)
    e4 = Edge((n4, n3), 'E', False, False)
    e5 = Edge((n2, n5), 'E', False, False)
    g.add_node(n1)
    g.add_node(n2)
    g.add_node(n3)
    g.add_node(n4)
    g.add_node(n5)
    g.add_edge(e1)
    g.add_edge(e2)
    g.add_edge(e3)
    g.add_edge(e4)
    g.add_edge(e5)

    draw(g)
    P0().apply(g)
    draw(g)


if __name__ == "__main__":
    example()
