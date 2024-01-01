def powerset(array, i, subset, subsets):
    if i == len(array):
        subsets.append(subset.copy())
    else:
        powerset(array, i + 1, subset + [array[i]], subsets)
        powerset(array, i + 1, subset, subsets)


def get_subsets(array):
    subsets = []
    subset = []
    powerset(array, 0, subset, subsets)
    return subsets


print(get_subsets([1, 2, 3]))
