from collections import deque

def is_visited(state, visited):
    return state in visited

def water_jug_bfs():
    max_a, max_b = 5, 4
    visited = set()
    queue = deque()
    queue.append((0, 0))

    while queue:
        a, b = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        print(f"Jug A: {a}L , Jug B: {b}L")

        if a == 2 or b == 2:
            print("Found a Solution!")
            return

        pour_b_to_a = min(a + b, max_a)
        pour_a_to_b = min(a + b, max_b)

        possible_states = [
            (max_a, b),
            (a, max_b),
            (0, b),
            (a, 0),
            (pour_b_to_a, b - (pour_b_to_a - a)),
            (a - (pour_a_to_b - b), pour_a_to_b)
        ]

        for state in possible_states:
            if not is_visited(state, visited):
                queue.append(state)

    print("No Solution found")

water_jug_bfs()