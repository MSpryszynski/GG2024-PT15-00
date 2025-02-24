import networkx as nx
from structure.graph import Graph
import matplotlib.pyplot as plt


def draw(g: Graph) -> None:
    coords = {node: (node.x, node.y) for node in g.get_nodes()}
    label_positions = {node: (x, y + 0.05) for node, (x, y) in coords.items()}
    labels = {node: (f"{node.label}"
                     f"{', h=' if not node.hyper else ''}"f"{1 if node.h and not node.hyper else ''}{0 if not node.h and not node.hyper else ''}"
                     f"{', r=' if node.hyper else ''}"f"{1 if node.hyper_r and node.hyper else ''}{0 if not node.hyper_r and node.hyper else ''}")
              for node in g.get_nodes()}

    nx.draw_networkx_nodes(g.get(), coords, node_size=200, edgecolors="black", linewidths=2, alpha=0.5)
    nx.draw_networkx_edges(g.get(), coords, width=3, alpha=0.3)
    nx.draw_networkx_labels(g.get(), label_positions, labels)

    edge_labels = {}
    for u, v in g.get_edges():
        if not u.hyper and not v.hyper:
            edge = g.get().get_edge_data(u, v)
            if "boundary" in edge:
                edge_labels[(u, v)] = f"b={'1' if edge['boundary'] else '0'}"

    nx.draw_networkx_edge_labels(
        g.get(), pos=coords, edge_labels=edge_labels, font_size=8
    )

    ax = plt.gca()
    ax.margins(0.15)
    plt.tight_layout()
    plt.axis("off")
    plt.show()
    plt.cla()
    plt.clf()
