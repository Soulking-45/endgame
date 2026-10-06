graph = {
    "A": ({"B": 1, "E": 3, "D": 2}, 4),
    "B": ({"D": 1, "C": 2}, 3),
    "C": ({"F": 3}, 2),
    "D": ({"F": 2}, 3),
    "E": ({"D": 3, "F": 4}, 2),
    "F": ({}, 0),
}

def get_min(q):
    mn = None
    for i in q:
        if mn is None or sum(q[i]) < sum(q[mn]):
            mn = i
    return mn

def a_star(graph, prev, des, path, pcost, q, visited):
    print("Connected nodes of current node", prev, "with h(n) value:")
    for n in graph[prev][0]:
        if n not in path and n not in visited:
            # q[n] stores (heuristic, edge cost)
            q[n] = (graph[n][1], graph[prev][0][n])
            print(n, "->", q[n])
            add1 = sum(q[n])
            path_cost = pcost + add1
            print("A* value for", n, "is:", path_cost)

    while q:
        mn = get_min(q)
        q.pop(mn)  
        print("selection minimum vertex:", mn)
        print("--------------------------")
        if des == mn:
            return path + [des]

        visited.add(mn)  
        pc = pcost + sum(graph[mn][0].values()) if graph[mn][0] else pcost
        print("previous path cost:", pc)

        new_path = a_star(graph, mn, des, path + [mn], pc, q, visited)
        if new_path:
            return new_path

    return []


source = input("Enter source vertex: ")
des = input("Enter destination vertex: ")
path = a_star(graph, source, des, [source], 0, {}, set())
if path:
    print("Final path:", path)
else:
    print("Path not found!")
#A and F input
