def binary_search(low, high, target):
    print('In Function')
    if low > high:
        print('Not Found')
    else:
        mid = (low + high) // 2
        if num_list[mid] == target:
            print(f'\nFound the target!\n{target} -> {num_list.index(target) + 1}th item in your list')
        elif num_list[mid] > target:
            high = mid - 1
            binary_search(low, high, target)
        elif num_list[mid] < target:
            low = mid + 1
            binary_search(low, high, target)


num_list = [10, 12, 13, 14, 18, 20, 25, 27, 30, 35, 40, 45]

# if we get an unsorted list (by getting the list by an input), it will be sorted by the following line
# num_list.sort()

print(num_list)
x = int(input('What are you looking for? '))
start_list = 0
end_list = len(num_list) - 1
binary_search(start_list, end_list, x)
