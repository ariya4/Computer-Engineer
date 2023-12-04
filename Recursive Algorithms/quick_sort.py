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
                temp = lst[j]
                lst[j] = lst[i]
                lst[i] = temp
        lst[pivot_index] = lst[j]
        lst[j] = pivot
        left_list = lst[:j]
        right_list = lst[j + 1:]
        return quick_sort(left_list) + [lst[j]] + quick_sort(right_list)


# یک روش دیگه برای حساب انجام الگوریتم غیر مراحلی که سر کلاس گفتیم
def quick_sort2(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[0]
    left = []
    middle = []
    right = []
    for i in lst:
        if i == pivot:
            middle.append(i)
        elif i > pivot:
            right.append(i)
        else:
            left.append(i)

    return quick_sort2(left) + middle + quick_sort2(right)


my_list = [5, 8, 9, 2, 1, 45, 12, 2]
print(my_list)
print('Method 1:', quick_sort(my_list))
print('Method 2:', quick_sort2(my_list))
