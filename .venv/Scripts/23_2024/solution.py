from collections import defaultdict

def parse_connections(filename):
    """Reads the connections from a file and returns a graph representation."""
    graph = defaultdict(set)
    with open(filename, 'r') as file:
        for line in file:
            a, b = line.strip().split('-')
            graph[a].add(b)
            graph[b].add(a)
    return graph

def find_triads(graph):
    """Finds all sets of three inter-connected computers."""
    triads = set()
    for node in graph:
        neighbors = graph[node]
        for neighbor1 in neighbors:
            for neighbor2 in neighbors:
                if neighbor1 != neighbor2 and neighbor2 in graph[neighbor1]:
                    triad = tuple(sorted([node, neighbor1, neighbor2]))
                    triads.add(triad)
    return triads

def filter_triads_with_t(triads):
    """Filters triads to include only those with at least one computer name starting with 't'."""
    return [triad for triad in triads if any(comp.startswith('t') for comp in triad)]

def find_largest_clique(graph):
    """Finds the largest clique in the graph using a more efficient approach."""
    def bron_kerbosch(r, p, x, cliques):
        if not p and not x:
            cliques.append(r)
            return
        for v in list(p):
            bron_kerbosch(r.union([v]), p.intersection(graph[v]), x.intersection(graph[v]), cliques)
            p.remove(v)
            x.add(v)

    nodes = set(graph.keys())
    cliques = []
    bron_kerbosch(set(), nodes, set(), cliques)
    largest_clique = max(cliques, key=len) if cliques else []
    return sorted(largest_clique)

def get_lan_party_password(clique):
    """Generates the LAN party password from the clique."""
    return ','.join(sorted(clique))

def main():
    filename = 'input.txt'
    graph = parse_connections(filename)

    # Part 1
    triads = find_triads(graph)
    filtered_triads = filter_triads_with_t(triads)
    print("Total triads containing at least one 't':", len(filtered_triads))
    print("Triads:", filtered_triads)

    # Part 2
    largest_clique = find_largest_clique(graph)
    password = get_lan_party_password(largest_clique)
    print("Largest clique:", largest_clique)
    print("LAN party password:", password)

if __name__ == "__main__":
    main()
