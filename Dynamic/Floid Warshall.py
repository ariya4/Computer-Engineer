def floyd_warshall(graph):
    V = len(graph)

    # Create a copy of the graph to store the shortest distances
    dist = [row[:] for row in graph]

    # Update the distance matrix
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


# Example usage:
# Define an example graph with weighted edges.
# 'inf' represents infinity (no direct edge).
inf = float('inf')
graph = [
    [0, 3, inf, 7],
    [8, 0, 2, inf],
    [5, inf, 0, 1],
    [2, inf, inf, 0]
]

# Find the shortest distances between all pairs of vertices
result = floyd_warshall(graph)

# Print the result
for row in result:
    print(row)
