from plotting.plot import draw
from productions.p8 import P8
from structure.graph import Graph
from structure.hyperedge import HyperEdge
from structure.node import Node
from tests.test import Test


def case1():
    g = Graph()
    n1 = Node(0, 0, "N1", h=True)
    n2 = Node(1, 0, "N2")
    n3 = Node(1, 1, "N3")
    n4 = Node(0, 1, "N4")
    n5 = Node(1, 0.5, "N5", h=True)
    n6 = Node(2, 0.5, "N6", h=True)
    n7 = Node(2, 1, "N7", h=True)

    for n in [n1, n2, n3, n4, n5, n6, n7]:
        g.add_node(n)

    edges = [
        (n2, n5, True), (n5, n3, True),
    ]

    for u, v, b_param in edges:
        g.add_edge(HyperEdge((u, v), "E", b=b_param))

    hyper_edges = [
        [(n1, n2, n3, n4), False], [(n5, n6, n7, n3), True]
    ]

    for nodes, r in hyper_edges:
        u, v, w, x = nodes
        g.add_hyper_edge(HyperEdge((u, v, w, x), "Q", r=r))

    draw(g)
    P8().apply(g)
    draw(g)


def case2():
    g = Graph()
    n1 = Node(0, 0, "N1", h=True)
    n2 = Node(1, 0, "N2")
    n3 = Node(1, 1, "N3")
    n4 = Node(0, 1, "N4")
    n5 = Node(1, 0.5, "N5", h=True)
    n6 = Node(2, 0.5, "N6", h=True)
    n7 = Node(2, 1, "N7", h=True)

    for n in [n1, n2, n3, n4, n5, n6, n7]:
        g.add_node(n)

    edges = [
        (n2, n5, True), (n5, n3, True), (n1, n4, False),
    ]

    for u, v, b_param in edges:
        g.add_edge(HyperEdge((u, v), "E", b=b_param))

    hyper_edges = [
        [(n1, n2, n3, n4), False], [(n5, n6, n7, n3), True]
    ]

    for nodes, r in hyper_edges:
        u, v, w, x = nodes
        g.add_hyper_edge(HyperEdge((u, v, w, x), "Q", r=r))

    draw(g)
    P8().apply(g)
    draw(g)


def case3():
    g = Graph()
    n1 = Node(0, 0, "N1", h=True)
    n2 = Node(1, 0, "N2")
    n3 = Node(1, 1, "N3")
    n4 = Node(0, 1, "N4")
    n5 = Node(1, 0.5, "N5", h=True)
    n6 = Node(2, 0.5, "N6", h=True)
    n7 = Node(2, 1, "N7", h=True)

    for n in [n1, n2, n3, n4, n5, n6, n7]:
        g.add_node(n)

    edges = [
        (n2, n5, True), (n5, n3, True), (n1, n4, False),
    ]

    for u, v, b_param in edges:
        g.add_edge(HyperEdge((u, v), "E", b=b_param))

    hyper_edges = [
        [(n1, n2, n3, n4), False], [(n5, n6, n7, n3), True]
    ]

    for nodes, r in hyper_edges:
        u, v, w, x = nodes
        g.add_hyper_edge(HyperEdge((u, v, w, x), "Q", r=r))

    draw(g)
    P8().apply(g)
    draw(g)


def case4():
    g = Graph()
    n1 = Node(0, 0, "N1", h=True)
    n2 = Node(1, 0, "N2")
    n3 = Node(1, 1, "N3")
    n4 = Node(0, 1, "N4")
    n5 = Node(1, 0.5, "N5", h=True)
    n6 = Node(2, 0.5, "N6", h=True)
    n7 = Node(2, 1, "N7", h=True)

    for n in [n1, n2, n3, n4, n5, n6, n7]:
        g.add_node(n)

    edges = [
        (n2, n5, True), (n5, n3, True), (n1, n4, False), (n1, n2, True),
        (n6, n7, True)
    ]

    for u, v, b_param in edges:
        g.add_edge(HyperEdge((u, v), "E", b=b_param))

    hyper_edges = [
        [(n1, n2, n3, n4), False], [(n5, n6, n7, n3), True]
    ]

    for nodes, r in hyper_edges:
        u, v, w, x = nodes
        g.add_hyper_edge(HyperEdge((u, v, w, x), "Q", r=r))

    draw(g)
    P8().apply(g)
    draw(g)


def case5():
    g = Graph()
    n1 = Node(0, 0, "N1", h=True)
    n2 = Node(1, 0, "N2")
    n3 = Node(1, 1, "N3")
    n4 = Node(0, 1, "N4")
    n5 = Node(1, 0.5, "N5", h=False)
    n6 = Node(2, 0.5, "N6", h=True)
    n7 = Node(2, 1, "N7", h=True)

    for n in [n1, n2, n3, n4, n5, n6, n7]:
        g.add_node(n)

    edges = [
        (n2, n5, True), (n5, n3, True), (n1, n4, False), (n1, n2, True),
        (n6, n7, True)
    ]

    for u, v, b_param in edges:
        g.add_edge(HyperEdge((u, v), "E", b=b_param))

    hyper_edges = [
        [(n1, n2, n3, n4), False], [(n5, n6, n7, n3), True]
    ]

    for nodes, r in hyper_edges:
        u, v, w, x = nodes
        g.add_hyper_edge(HyperEdge((u, v, w, x), "Q", r=r))

    draw(g)
    P8().apply(g)
    draw(g)


def case6():
    g = Graph()
    n1 = Node(0, 0, "N1", h=True)
    n2 = Node(1, 0, "N2")
    n3 = Node(1, 1, "N3")
    n4 = Node(0, 1, "N4")
    n5 = Node(1, 0.5, "N5", h=True)
    n6 = Node(2, 0.5, "N6", h=True)
    n7 = Node(2, 0, "N7", h=True)

    for n in [n1, n2, n3, n4, n5, n6, n7]:
        g.add_node(n)

    edges = [
        (n2, n5, True), (n5, n3, True),
    ]

    for u, v, b_param in edges:
        g.add_edge(HyperEdge((u, v), "E", b=b_param))

    hyper_edges = [
        [(n1, n2, n3, n4), False], [(n5, n6, n7, n2), True]
    ]

    for nodes, r in hyper_edges:
        u, v, w, x = nodes
        g.add_hyper_edge(HyperEdge((u, v, w, x), "Q", r=r))

    draw(g)
    P8().apply(g)
    draw(g)


def case7():
    g = Graph()
    n1 = Node(0, 0, "N1", h=True)
    n2 = Node(1, 0, "N2")
    n3 = Node(1, 1, "N3")
    n4 = Node(0, 1, "N4")
    n5 = Node(1, 0.5, "N5", h=True)
    n6 = Node(2, 0.5, "N6", h=True)
    n7 = Node(2, 0, "N7", h=True)

    for n in [n1, n2, n3, n4, n5, n6, n7]:
        g.add_node(n)

    edges = [
        (n2, n5, True), (n5, n3, True),
    ]

    for u, v, b_param in edges:
        g.add_edge(HyperEdge((u, v), "E", b=b_param))

    hyper_edges = [
        [(n1, n2, n3, n4), False], [(n5, n6, n7, n2), False]
    ]

    for nodes, r in hyper_edges:
        u, v, w, x = nodes
        g.add_hyper_edge(HyperEdge((u, v, w, x), "Q", r=r))

    draw(g)
    P8().apply(g)
    draw(g)


def case8():
    g = Graph()
    n1 = Node(0, 0, "N1", h=True)
    n2 = Node(1, 0, "N2")
    n3 = Node(1, 1, "N3")
    n4 = Node(0, 1, "N4")
    n5 = Node(1, 0.5, "N5", h=True)
    n6 = Node(2, 0.5, "N6", h=True)
    n7 = Node(2, 0, "N7", h=True)
    nt1 = Node(0, -1, "T1", h=True)
    nt2 = Node(2, -1, "T2", h=True)

    for n in [n1, n2, n3, n4, n5, n6, n7, nt1, nt2]:
        g.add_node(n)

    edges = [
        (n2, n5, True), (n5, n3, True),
    ]

    for u, v, b_param in edges:
        g.add_edge(HyperEdge((u, v), "E", b=b_param))

    hyper_edges = [
        [(n1, n2, n3, n4), False], [(n5, n6, n7, n2), True],
        [(n1, n7, nt1, nt2), True]
    ]

    for nodes, r in hyper_edges:
        u, v, w, x = nodes
        g.add_hyper_edge(HyperEdge((u, v, w, x), "Q", r=r))

    draw(g)
    P8().apply(g)
    draw(g)


class T8(Test):
    @staticmethod
    def run():
        # case1()
        # case2()
        # case3()
        # case4()
        # case5()
        # case6()
        # case7()
        case8()
