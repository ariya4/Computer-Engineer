import random


def binary_search(low, high, target, lst):
    print('In Function')
    if low > high:
        return 'Not Found!'
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


user_range = int(input("Enter the range: "))
user_sample = int(input("Enter number of samples: "))
num_list = random.choices(range(user_range), k=user_sample)
num_list.sort()
print(num_list)

x = int(input('What are you looking for? '))
start_list = 0
end_list = len(num_list) - 1
print(binary_search(start_list, end_list, x, num_list))
