tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [4, 3],
    'E': [6, 2],
    'F': [2, 1],
    'G': [9, 5]
}

def minimax_alpha_beta(node, depth, alpha, beta, max_player):

    if depth == 0 or node not in tree:
        if node in tree:
            return tree[node][0]
        else:
            return node

    if max_player:
        value = -float('inf')

        for child in tree[node]:
            value = max(
                value,
                minimax_alpha_beta(
                    child, depth - 1, alpha, beta, False
                )
            )

            alpha = max(alpha, value)

            if alpha >= beta:
                print(f"Pruning branch at node {node}")
                break

        return value

    else:
        value = float('inf')

        for child in tree[node]:
            value = min(
                value,
                minimax_alpha_beta(
                    child, depth - 1, alpha, beta, True
                )
            )

            beta = min(beta, value)

            if beta <= alpha:
                print(f"Pruning branch at node {node}")
                break

        return value


best_score = minimax_alpha_beta(
    'A',
    2,
    -float('inf'),
    float('inf'),
    True
)

print(f"The best score is {best_score}")