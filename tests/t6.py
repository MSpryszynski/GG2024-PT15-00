from plotting.plot import draw
from productions.p6 import P6
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
    n8 = Node(0.5, 1, "N8", h=True)

    for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
        g.add_node(n)

    edges = [
        (n1, n6, True), (n6, n2, True), (n2, n5, False), (n5, n3, False),
        (n3, n8, False), (n8, n4, False), (n4, n7, True), (n7, n1, True)
    ]

    for u, v, b_param in edges:
        g.add_edge(HyperEdge((u, v), "E", b=b_param))

    hyper_edge = HyperEdge((n1, n2, n3, n4), 'E', r=True)
    g.add_hyper_edge(hyper_edge)

    draw(g)
    P6().apply(g)
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
    n8 = Node(0.5, 1, "N8", h=True)

    for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
        g.add_node(n)

    edges = [
        (n1, n6, True), (n6, n2, True), (n2, n5, False), (n5, n3, False),
        (n3, n8, False), (n8, n4, False), (n4, n7, True), (n7, n1, True)
    ]

    for u, v, b_param in edges:
        g.add_edge(HyperEdge((u, v), "E", b=b_param))

    hyper_edge = HyperEdge((n1, n2, n3, n4), 'E', r=False)
    g.add_hyper_edge(hyper_edge)

    draw(g)
    P6().apply(g)
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
    n8 = Node(0.5, 1, "N8", h=True)
    nt1 = Node(0, 2, "T1")
    nt2 = Node(1, 2, "T2")
    nt3 = Node(0, 1.5, "T3", h=True)
    nt4 = Node(1, 1.5, "T4", h=True)
    nt5 = Node(0.5, 2, "T5", h=True)

    for n in [n1, n2, n3, n4, n5, n6, n7, n8, nt1, nt2, nt3, nt4, nt5]:
        g.add_node(n)

    edges = [
        (n1, n6, False), (n6, n2, False), (n2, n5, True), (n5, n3, True),
        (n3, n8, False), (n8, n4, False), (n4, n7, False), (n7, n1, False),
        (n4, nt3, True), (nt3, nt1, True), (nt1, nt5, False),
        (nt5, nt2, False), (nt2, nt4, False), (nt4, n3, False)
    ]

    for u, v, b_param in edges:
        g.add_edge(HyperEdge((u, v), "E", b_param))

    hyper_egdes = [
        [(n1, n2, n3, n4), True], [(nt1, nt2, n3, n4), True]
    ]
    for nodes, r in hyper_egdes:
        g.add_hyper_edge(HyperEdge(nodes, 'E', r=r))

    draw(g)
    P6().apply(g)
    draw(g)
    P6().apply(g)
    draw(g)


def case4():
    g = Graph()
    n1 = Node(0, 0, "N1")
    n2 = Node(1, 0, "N2")
    n3 = Node(1, 1, "N3")
    n4 = Node(0, 1, "N4")
    n5 = Node(1, 0.5, "N5", h=True)
    n6 = Node(0.5, 0, "N6", h=False)
    n7 = Node(0, 0.5, "N7", h=True)
    n8 = Node(0.5, 1, "N8", h=True)

    for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
        g.add_node(n)

    edges = [
        (n1, n6, True), (n6, n2, True), (n2, n5, False), (n5, n3, False),
        (n3, n8, False), (n8, n4, False), (n4, n7, True), (n7, n1, True)
    ]

    for u, v, b_param in edges:
        g.add_edge(HyperEdge((u, v), "E", b=b_param))

    hyper_edge = HyperEdge((n1, n2, n3, n4), 'E', r=True)
    g.add_hyper_edge(hyper_edge)

    draw(g)
    P6().apply(g)
    draw(g)


def case4():
    g = Graph()
    n1 = Node(0, 0, "N1")
    n2 = Node(1, 0, "N2")
    n3 = Node(1, 1, "N3")
    n4 = Node(0, 1, "N4")
    n5 = Node(1, 0.5, "N5", h=True)
    n6 = Node(0.5, 0, "N6", h=False)
    n7 = Node(0, 0.5, "N7", h=True)
    n8 = Node(0.5, 1, "N8", h=True)

    for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
        g.add_node(n)

    edges = [
        (n1, n6, True), (n6, n2, True), (n2, n5, False), (n5, n3, False),
        (n3, n8, False), (n8, n4, False), (n4, n7, True), (n7, n1, True)
    ]

    for u, v, b_param in edges:
        g.add_edge(HyperEdge((u, v), "E", b=b_param))

    hyper_edge = HyperEdge((n1, n2, n3, n4), 'E', r=True)
    g.add_hyper_edge(hyper_edge)

    draw(g)
    P6().apply(g)
    draw(g)

def case5():
    g = Graph()
    n1 = Node(0, 0, "N1")
    n2 = Node(1, 0, "N2")
    n3 = Node(1, 1, "N3")
    n4 = Node(0, 1, "N4")
    n5 = Node(1, 0.5, "N5", h=True)
    n6 = Node(0.5, 0, "N6", h=True)
    n7 = Node(0, 0.5, "N7", h=True)
    n8 = Node(0.5, 1, "N8", h=False)
    nt1 = Node(0, 2, "T1")
    nt2 = Node(1, 2, "T2")
    nt3 = Node(0, 1.5, "T3", h=True)
    nt4 = Node(1, 1.5, "T4", h=True)
    nt5 = Node(0.5, 2, "T5", h=True)

    for n in [n1, n2, n3, n4, n5, n6, n7, n8, nt1, nt2, nt3, nt4, nt5]:
        g.add_node(n)

    edges = [
        (n1, n6, False), (n6, n2, False), (n2, n5, True), (n5, n3, True),
        (n3, n8, False), (n8, n4, False), (n4, n7, False), (n7, n1, False),
        (n4, nt3, True), (nt3, nt1, True), (nt1, nt5, False),
        (nt5, nt2, False), (nt2, nt4, False), (nt4, n3, False)
    ]

    for u, v, b_param in edges:
        g.add_edge(HyperEdge((u, v), "E", b_param))

    hyper_egdes = [
        [(n1, n2, n3, n4), True], [(nt1, nt2, n3, n4), True]
    ]
    for nodes, r in hyper_egdes:
        g.add_hyper_edge(HyperEdge(nodes, 'E', r=r))

    draw(g)
    P6().apply(g)
    draw(g)
    P6().apply(g)
    draw(g)

def case6():
    g = Graph()
    n1 = Node(0, 0, "N1")
    n2 = Node(1, 0, "N2")
    n3 = Node(1, 1, "N3")
    n4 = Node(0, 1, "N4", h=True)
    n5 = Node(1, 0.5, "N5", h=True)
    n6 = Node(0.5, 0, "N6", h=True)
    n7 = Node(0, 0.5, "N7", h=True)
    n8 = Node(0.5, 1, "N8", h=True)
    nt1 = Node(0, 2, "T1")
    nt2 = Node(1, 2, "T2")
    nt3 = Node(0, 1.5, "T3", h=True)
    nt4 = Node(1, 1.5, "T4", h=True)
    nt5 = Node(0.5, 2, "T5", h=True)

    for n in [n1, n2, n3, n4, n5, n6, n7, n8, nt1, nt2, nt3, nt4, nt5]:
        g.add_node(n)

    edges = [
        (n1, n6, False), (n6, n2, False), (n2, n5, True), (n5, n3, True),
        (n3, n8, False), (n8, n4, False), (n4, n7, False), (n7, n1, False),
        (n4, nt3, True), (nt3, nt1, True), (nt1, nt5, False),
        (nt5, nt2, False), (nt2, nt4, False), (nt4, n3, False)
    ]

    for u, v, b_param in edges:
        g.add_edge(HyperEdge((u, v), "E", b_param))

    hyper_egdes = [
        [(n1, n2, n3, n4), True], [(nt1, nt2, n3, n4), True]
    ]
    for nodes, r in hyper_egdes:
        g.add_hyper_edge(HyperEdge(nodes, 'E', r=r))

    draw(g)
    P6().apply(g)
    draw(g)
    P6().apply(g)
    draw(g)


class T6(Test):
    @staticmethod
    def run():
        # case1()
        # case2()
        # case3()
        # case4()
        case5()
        # case6() # !!!
