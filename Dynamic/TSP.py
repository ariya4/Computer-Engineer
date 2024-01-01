# Traveling Saleman Problem
inf = float('inf')

cities = ['v1', 'v2', 'v3', 'v4']
graph = [
    [0, 2, 9, inf],
    [1, 0, 6, 4],
    [inf, 7, 0, 8],
    [6, 3, inf, 0],
]


# aval tamam subset ha ro mohasebe mikonim
def generate_subsets(lst):
    subsets = [[]]
    for i in lst:
        subsets += [current + [i] for current in subsets]
    return subsets


power_set = generate_subsets(cities)
for subset in power_set:
    # print(subset)
    if 'v1' not in subset:
        # print(subset)
        if 'v2' not in subset:
            print(subset)

