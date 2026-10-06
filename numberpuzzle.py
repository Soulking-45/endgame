from collections import deque

goal = '123456780'

moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def bfs(start):
    visited = set()
    queue = deque([(start, [])])
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path + [state]
        if state in visited:
            continue
        visited.add(state)
        zero = state.index('0')
        for move in moves[zero]:
            new_state = list(state)
            
            new_state[zero], new_state[move] = new_state[move], new_state[zero]
            new_state = ''.join(new_state)
            queue.append((new_state, path + [state]))
    return None


start = input("Enter the start state (9 digits, use 0 for blank): ")
selection = bfs(start)

if selection:
    print("Steps to solve:")
    step_num = 1
    for s in selection:
        print(f"Step {step_num}:")
        print(s[0:3])
        print(s[3:6])
        print(s[6:9])
        print("---")
        step_num += 1
else:
    print("No Solution found :)")
