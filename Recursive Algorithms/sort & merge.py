import random

# benchmark
user_range = int(input("Enter the range: "))
user_sample = int(input("Enter number of samples: "))
num_list = random.choices(range(user_range), k=user_sample)
print(f'Original list: {num_list}')


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_list = lst[:mid]
    right_list = lst[mid:]
    # print('in split left', left_list)
    # print('in split right', right_list)
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return merge(left_list, right_list)


def merge(L, R):
    # print('in merge left', L)
    # print('in merge right', R)
    merged = []
    i = 0
    j = 0

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            merged.append(L[i])
            i += 1
        else:
            merged.append(R[j])
            j += 1
    for i in range(i, len(L)):
        merged.append(L[i])
    # merged.extend(L[i:])

    for i in range(j, len(R)):
        merged.append(R[i])
    # merged.extend(R[j:])

    # print('merged list', merged)
    return merged


print('Sorted List:', merge_sort(num_list))
