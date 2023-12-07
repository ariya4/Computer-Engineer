def recursive_power(x, n) -> int:
    if n == 0:
        return 1
    if n % 2 == 0:
        temp = (recursive_power(x, n // 2)) ** 2
        return temp
    elif n % 2 == 1:
        temp = x * recursive_power(x, n-1)
        return temp


print(recursive_power(2, 10))
