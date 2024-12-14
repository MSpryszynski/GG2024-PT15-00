from networkx.algorithms.isomorphism import GraphMatcher
import networkx as nx


def find_isomorphisms(graph: nx.Graph, subgraph: nx.Graph) -> list[dict]:
    matcher = GraphMatcher(graph, subgraph,
                           node_match=lambda u, v: u["h"] == v["h"] and u["hyper_r"] == v["hyper_r"])
    processed_nodes = set()
    mappings_to_process = []
    mappings = sorted(list(matcher.subgraph_isomorphisms_iter()), key=lambda iso: "".join(node.label for node in iso.keys()))
    for iso_map in mappings:
        nodes_of_found_mapping = set(iso_map.keys())
        mapping_applicable = True
        for node in nodes_of_found_mapping:
            if node in processed_nodes:
                mapping_applicable = False
                break
        if mapping_applicable:
            mappings_to_process.append(iso_map)
            processed_nodes.update(nodes_of_found_mapping)
    return mappings_to_process
