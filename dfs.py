import collections

def dfs(g, n, seen, d):
    if n not in seen:
        seen.append(n)

        if n == d:
            return seen

        for i in g[n]:
            if seen[-1] == d:
                break
            dfs(g, i, seen, d)

    return seen


graph = {
    'M': ['R', 'Q', 'N'],
    'N': ['M', 'Q', 'O'],
    'O': ['N', 'P'],
    'R': ['M'],
    'Q': ['M', 'N', 'P']
}

print(dfs(graph, 'M', [], 'P'))