import random

distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]


def get_cost(tour):
    cost = 0

    for i in range(len(tour)):
        cost += distance[tour[i - 1]][tour[i]]

    print("Cost of tour:", cost)
    return cost


def get_neighbor(tour):
    a, b = random.sample(range(len(tour)), 2)

    tour[a], tour[b] = tour[b], tour[a]

    return tour


def hill_climb():
    current = [0, 1, 2, 3]
    random.shuffle(current)

    current_cost = get_cost(current)

    print("Starting tour:", current, "cost:", current_cost)

    for i in range(100):
        neighbor = current[:]

        print("Current neighbor:", neighbor)

        neighbor = get_neighbor(neighbor)

        print("Connected neighbor:", neighbor)

        neighbor_cost = get_cost(neighbor)

        if neighbor_cost < current_cost:
            current = neighbor[:]

            print("Current neighbor:", current)

            current_cost = neighbor_cost

            print("Current cost:", current_cost)

            print("Better tour found:", current, "cost:", current_cost)

    return current, current_cost


best_tour, best_cost = hill_climb()

print("Best tour:", best_tour)
print("Best cost:", best_cost)