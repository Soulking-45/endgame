graph = {
    "A": ({"A": 13}, 3),
    "B": ({"C": 23}, 12),
    "C": ({"G": 3}, 2),
    "D": ({"B": 33, "G": 2}, 4),
    "E": ({"G": 23}, 5),
    "S": ({"D": 13, "A": 2, "E": 3}, 6),
    "G": ({}, 0)
}

def greedy_search_rec(graph, prev, dst, path, q, visited):
    print("Connected nodes of current node", prev, "with h(n) value")
    for n in graph[prev][0]:
        if n not in path and n not in visited:
            q[n] = graph[n][1]   
            print(n, "->", q[n])

    while q:
        mn = min(q, key=q.get)   
        q.pop(mn)
        print("taking minimum h(n) vertex:", mn)
        if dst == mn:
            return path + [dst]

        visited.add(mn) 
        new_path = greedy_search_rec(graph, mn, dst, path + [mn], q, visited)
        if new_path:
            return new_path

    return []


source = input("Enter source vertex: ")
dst = input("Enter destination vertex: ")
path = greedy_search_rec(graph, source, dst, [source], {}, set())
if path:
    print("Final path:", path)
else:
    print("path not found!")

# S and G input