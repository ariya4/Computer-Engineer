import random


def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        j = 0
        pivot = lst[0]
        pivot_index = 0
        for i in range(1, len(lst)):
            if pivot < lst[i]:
                i += 1
            elif pivot > lst[i]:
                j += 1
                lst[j], lst[i] = lst[i], lst[j]
        lst[pivot_index] = lst[j]
        lst[j] = pivot
        left_list = lst[:j]
        right_list = lst[j + 1:]
        return quick_sort(left_list) + [lst[j]] + quick_sort(right_list)


# benchmark
my_list = random.choices(range(1000), k=20)
print(f'Original list: {my_list}')

print('Method 1:', quick_sort(my_list))
