def validTree(n, edges):
    from collections import defaultdict
    g = defaultdict(set)
    for i in range(n): g[i]  # O(V)
    for u, v in edges:  # O(E)
        g[u].add(v)
        g[v].add(u)

    #         for k,v in g.items():
    #             print('{}: {}'.format(k,v))

    def visit(v):
        if v in visited: return False
        visited.add(v)
        path.add(v)
        for nbor in g[v]:
            if nbor not in visited:
                if (nbor in path) or visit(nbor):
                    return True
        path.remove(v)
        return False

    visited, path = set(), set()

    components = defaultdict(int)
    count = 0
    for vert in g:
        if visit(vert):
            return False  # there's a cycle if visit returns True
        print(visited)
        components[len(visited)] += 1

    print(len(components))

    # no cycle
    return len(edges) == n - 1 and len(visited) == n


validTree(5, [[0,1],[1,2],[3,4]])