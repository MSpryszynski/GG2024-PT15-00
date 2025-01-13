from networkx.algorithms.isomorphism import GraphMatcher
import networkx as nx


def node_matcher(u, v):
    if u["h"] is None or v["h"] is None:
        return True
    return u["h"] == v["h"] and u["hyper_r"] == v["hyper_r"] and u["hyper"] == v["hyper"]


def find_isomorphisms(graph: nx.Graph, subgraph: nx.Graph) -> list[dict]:
    matcher = GraphMatcher(graph, subgraph,
                           node_match=node_matcher)
    distinct_mappings = []
    seen_labels = set()
    mappings = sorted(list(matcher.subgraph_monomorphisms_iter()), key=lambda iso: "".join(node.label for node in iso.keys()))
    for iso_map in mappings:
        labels = tuple(sorted(node.label for node in iso_map.keys()))
        if labels not in seen_labels:
            seen_labels.add(labels)
            distinct_mappings.append(iso_map)
    for index, iso_map in enumerate(distinct_mappings):
        labels = [node.label for node in iso_map.keys()]
        print(f"Mapping {index}: {labels}")

    selected_index = int(input("Pick the index of the mapping to process: "))
    selected_mapping = distinct_mappings[selected_index]

    return selected_mapping
