def recursive_power(x, n) -> int:
    if n == 0:
        return 1
    if n % 2 == 0:
        return (recursive_power(x, n // 2)) ** 2
    elif n % 2 == 1:
        return x * recursive_power(x, n - 1)


base = int(input('Enter your base number (x ** n % p) --> x: '))
power = int(input('Enter your power number (x ** n % p) --> n: '))
module = int(input('Enter your base number (x ** n % p) --> p: '))

print(f'Remainder is: {recursive_power(base, power) % module}')
