# Use a large value to represent infinity
inf = float('inf')

def tsp_dynamic_directed(graph):
    num_cities = len(graph)
    all_cities = set(range(num_cities))

    # memoization table to store solutions to subproblems
    memo = {}

    # function to compute the minimum cost of visiting all cities starting from city 0
    def min_cost(curr, remaining):
        if not remaining:
            return graph[curr][0], [0]  # return cost and route

        if (curr, remaining) in memo:
            return memo[(curr, remaining)]

        min_val = float('inf')
        optimal_route = []

        for next_city in remaining:
            new_remaining = tuple(city for city in remaining if city != next_city)
            cost, route = min_cost(next_city, new_remaining)
            cost += graph[curr][next_city]

            if cost < min_val:
                min_val = cost
                optimal_route = [curr] + route

        memo[(curr, remaining)] = (min_val, optimal_route)
        return min_val, optimal_route

    # initialize remaining cities (excluding starting city)
    remaining_cities = tuple(city for city in range(1, num_cities))

    # start the recursion from the starting city (0)
    min_cost_tsp, optimal_route_tsp = min_cost(0, remaining_cities)

    return min_cost_tsp, optimal_route_tsp

# Example usage:
# Replace this graph with your own adjacency matrix or distance matrix
graph_example_directed = [
    [inf, 10, 15, 20],
    [inf, inf, 35, 25],
    [15, 35, inf, 30],
    [20, 25, 30, inf]
]

min_cost_tsp_directed, optimal_route_tsp_directed = tsp_dynamic_directed(graph_example_directed)
print("Minimum Cost of Directed TSP (Dynamic Programming):", min_cost_tsp_directed)
print("Optimal Route:", optimal_route_tsp_directed)
