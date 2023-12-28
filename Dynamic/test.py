def generate_subsets(nums):
    subsets = []
    n = len(nums)
    for i in range(1 << n):  # Iterate through 2^n possible subsets
        subset = [nums[j] for j in range(n) if (i & (1 << j))]  # Check each bit in i to include elements
        subsets.append(subset)
    return subsets


# Example set
example_set = [1, 2, 4, {3, 4}, 7]

# Generating subsets
all_subsets = generate_subsets(example_set)

# Displaying subsets
for subset in all_subsets:
    print(subset)
print(all_subsets)
