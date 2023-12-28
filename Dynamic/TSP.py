inf = float('inf')


def tsp_dp(graphh):
    n = len(graphh)
    # Store subproblem solutions
    memo = [[None] * (1 << n) for _ in range(n)]

    # Helper function to solve TSP using DP
    def tsp(mask, pos):
        if mask == (1 << n) - 1:
            return graphh[pos][0] if graphh[pos][0] != inf else inf

        if memo[pos][mask] is not None:
            return memo[pos][mask]

        min_costt = inf
        for city in range(n):
            if (mask & (1 << city)) == 0 and graphh[pos][city] != inf:
                new_cost = graphh[pos][city] + tsp(mask | (1 << city), city)
                min_costt = min(min_costt, new_cost)

        memo[pos][mask] = min_costt
        return min_costt

    # Start from the 0th city
    return tsp(1, 0)


# Example usage:
# Define your graph (cost matrix with directions)
# For example, consider 4 cities:
# 0 10 15 20
# ∞ ∞ 35 25
# 15 ∞ ∞ 30
# 20 25 30 ∞
graph = [
    [0, 10, 15, 20],
    [inf, 0, 35, 25],
    [15, inf, 0, 30],
    [20, 25, 30, 0],
]

# Calculate TSP using dynamic programming
min_cost = tsp_dp(graph)
print(f"The minimum cost for TSP with directions is: {min_cost}")
