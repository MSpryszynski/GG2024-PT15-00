from plotting.plot import draw
from productions.p5 import P5
from structure.graph import Graph
from structure.hyperedge import HyperEdge
from structure.node import Node
from tests.test import Test


def case1():
    g = Graph()
    n1 = Node(0, 0, "N1")
    n2 = Node(1, 0, "N2")
    n3 = Node(1, 1, "N3")
    n4 = Node(0, 1, "N4")
    n5 = Node(1, 0.5, "N5", h=True)
    n6 = Node(0.5, 0, "N6", h=True)
    n7 = Node(0, 0.5, "N7", h=True)

    for n in [n1, n2, n3, n4, n5, n6, n7]:
        g.add_node(n)

    edges = [
        (n1, n6, False), (n6, n2, False), (n2, n5, True), (n5, n3, True),
        (n3, n4, False), (n4, n7, False), (n7, n1, False)
    ]

    for u, v, b_param in edges:
        g.add_edge(HyperEdge((u, v), "E", b_param))

    hyper_edge = HyperEdge((n1, n2, n3, n4), 'E', r=True)
    g.add_hyper_edge(hyper_edge)

    draw(g)
    P5().apply(g)
    draw(g)


def case2():
    g = Graph()
    n1 = Node(0, 0, "N1")
    n2 = Node(1, 0, "N2")
    n3 = Node(1, 1, "N3")
    n4 = Node(0, 1, "N4")
    n5 = Node(1, 0.5, "N5", h=True)
    n6 = Node(0.5, 0, "N6", h=True)
    n7 = Node(0, 0.5, "N7", h=True)
    nt1 = Node(0, 2, "T1")
    nt2 = Node(1, 2, "T2")
    nt3 = Node(0, 1.5, "T3", h=True)
    nt4 = Node(1, 1.5, "T4", h=True)

    for n in [n1, n2, n3, n4, n5, n6, n7, nt1, nt2, nt3, nt4]:
        g.add_node(n)

    edges = [
        (n1, n6, False), (n6, n2, False), (n2, n5, True), (n5, n3, True),
        (n3, n4, False), (n4, n7, False), (n7, n1, False), (n4, nt3, True),
        (nt3, nt1, True), (nt1, nt2, False), (nt2, nt4, False), (nt4, n3, False)
    ]

    for u, v, b_param in edges:
        g.add_edge(HyperEdge((u, v), "E", b_param))

    hyper_edges = [
        (n1, n2, n3, n4), (nt1, nt2, n3, n4)
    ]
    for x in hyper_edges:
        g.add_hyper_edge(HyperEdge(x, 'E', r=True))

    draw(g)
    P5().apply(g)
    draw(g)
    P5().apply(g)
    draw(g)


def case3():
    g = Graph()
    n1 = Node(0, 0, "N1")
    n2 = Node(1, 0, "N2")
    n3 = Node(1, 1, "N3")
    n4 = Node(0, 1, "N4")
    n5 = Node(1, 0.5, "N5", h=True)
    n6 = Node(0.5, 0, "N6", h=True)
    n7 = Node(0, 0.5, "N7", h=True)
    nt1 = Node(0, 2, "T1")
    nt2 = Node(1, 2, "T2")
    nt3 = Node(0, 1.5, "T3", h=False)
    nt4 = Node(1, 1.5, "T4", h=True)

    for n in [n1, n2, n3, n4, n5, n6, n7, nt1, nt2, nt3, nt4]:
        g.add_node(n)

    edges = [
        (n1, n6, False), (n6, n2, False), (n2, n5, True), (n5, n3, True),
        (n3, n4, False), (n4, n7, False), (n7, n1, False), (n4, nt3, True),
        (nt3, nt1, True), (nt1, nt2, False), (nt2, nt4, False), (nt4, n3, False)
    ]

    for u, v, b_param in edges:
        g.add_edge(HyperEdge((u, v), "E", b_param))

    hyper_edges = [
        (n1, n2, n3, n4), (nt1, nt2, n3, n4)
    ]
    for x in hyper_edges:
        g.add_hyper_edge(HyperEdge(x, 'E', r=True))

    draw(g)
    P5().apply(g)
    draw(g)
    P5().apply(g)
    draw(g)


def case4():
    g = Graph()
    n1 = Node(0, 0, "N1")
    n2 = Node(1, 0, "N2")
    n3 = Node(1, 1, "N3")
    n4 = Node(0, 1, "N4")
    n5 = Node(1, 0.5, "N5", h=True)
    n6 = Node(0.5, 0, "N6", h=True)
    n7 = Node(0, 0.5, "N7", h=True)
    nt1 = Node(0, 2, "T1", h=True) # !!!
    nt2 = Node(1, 2, "T2")
    nt3 = Node(0, 1.5, "T3", h=True)
    nt4 = Node(1, 1.5, "T4", h=True)

    for n in [n1, n2, n3, n4, n5, n6, n7, nt1, nt2, nt3, nt4]:
        g.add_node(n)

    edges = [
        (n1, n6, False), (n6, n2, False), (n2, n5, True), (n5, n3, True),
        (n3, n4, False), (n4, n7, False), (n7, n1, False), (n4, nt3, True),
        (nt3, nt1, True), (nt1, nt2, False), (nt2, nt4, False), (nt4, n3, False)
    ]

    for u, v, b_param in edges:
        g.add_edge(HyperEdge((u, v), "E", b_param))

    hyper_edges = [
        (n1, n2, n3, n4), (nt1, nt2, n3, n4)
    ]
    for x in hyper_edges:
        g.add_hyper_edge(HyperEdge(x, 'E', r=True))

    draw(g)
    P5().apply(g)
    draw(g)
    P5().apply(g)
    draw(g)



def case5():
    g = Graph()
    n1 = Node(0, 0, "N1")
    n2 = Node(1, 0, "N2")
    n3 = Node(1, 1, "N3")
    n4 = Node(0, 1, "N4")
    n5 = Node(1, 0.5, "N5", h=True)
    n6 = Node(0.5, 0, "N6", h=True)
    nt1 = Node(0, 2, "T1")
    nt2 = Node(1, 2, "T2")
    nt3 = Node(0, 1.5, "T3", h=True)
    nt4 = Node(1, 1.5, "T4", h=True)

    for n in [n1, n2, n3, n4, n5, n6, nt1, nt2, nt3, nt4]:
        g.add_node(n)

    edges = [
        (n1, n6, False), (n6, n2, False), (n2, n5, True), (n5, n3, True),
        (n3, n4, False), (n4, n1, False), (n4, nt3, True), (nt3, nt1, True),
        (nt1, nt2, False), (nt2, nt4, False), (nt4, n3, False)
    ]

    for u, v, b_param in edges:
        g.add_edge(HyperEdge((u, v), "E", b_param))

    hyper_edges = [
        (n1, n2, n3, n4), (nt1, nt2, n3, n4)
    ]
    for x in hyper_edges:
        g.add_hyper_edge(HyperEdge(x, 'E', r=True))

    draw(g)
    P5().apply(g)
    draw(g)


def case6():
    g = Graph()
    n1 = Node(0, 0, "N1")
    n2 = Node(1, 0, "N2")
    n3 = Node(1, 1, "N3")
    n4 = Node(0, 1, "N4")
    n5 = Node(1, 0.5, "N5", h=True)
    n6 = Node(0.5, 0, "N6", h=True)
    n7 = Node(0, 0.5, "N7", h=True)

    for n in [n1, n2, n3, n4, n5, n6, n7]:
        g.add_node(n)

    edges = [
        (n1, n6, False), (n6, n2, False), (n2, n5, True), (n5, n3, True),
        (n4, n7, False), (n7, n1, False)
    ]

    for u, v, b_param in edges:
        g.add_edge(HyperEdge((u, v), "E", b_param))

    hyper_edge = HyperEdge((n1, n2, n3, n4), 'E', r=True)
    g.add_hyper_edge(hyper_edge)

    draw(g)
    P5().apply(g)
    draw(g)


def case7():
    g = Graph()
    n1 = Node(0, 0, "N1")
    n2 = Node(1, 0, "N2")
    n3 = Node(1, 1, "N3")
    n4 = Node(0, 1, "N4")
    n5 = Node(1, 0.5, "N5", h=True)
    n6 = Node(0.5, 0, "N6", h=True)

    for n in [n1, n2, n3, n4, n5, n6]:
        g.add_node(n)

    edges = [
        (n1, n6, False), (n6, n2, False), (n2, n5, True), (n5, n3, True),
        (n3, n4, False), (n4, n1, False)
    ]

    for u, v, b_param in edges:
        g.add_edge(HyperEdge((u, v), "E", b_param))

    hyper_edge = HyperEdge((n1, n2, n3, n4), 'E', r=True)
    g.add_hyper_edge(hyper_edge)

    draw(g)
    P5().apply(g)
    draw(g)


class T5(Test):
    @staticmethod
    def run():
        case1()
        case2()
        case3()
        case4()
        case5()
        case6()
        case7()
