def binary_search(low, high, target, lst):
    print('In Function')
    if low > high:
        return 'Not Found'
    else:
        mid = (low + high) // 2
        if lst[mid] == target:
            return f'\nFound the target!\n{lst[mid]} -> {lst.index(target) + 1}th item in your list'
        elif lst[mid] > target:
            high = mid - 1
            return binary_search(low, high, target, lst)
        elif lst[mid] < target:
            low = mid + 1
            return binary_search(low, high, target, lst)


num_list = [10, 12, 13, 14, 18, 20, 25, 27, 30, 35, 40, 45]

# if we get an unsorted list (by getting the list by an input), it will be sorted by the following line
num_list.sort()

print(num_list)
x = int(input('What are you looking for? '))
start_list = 0
end_list = len(num_list) - 1
print(binary_search(start_list, end_list, x, num_list))
