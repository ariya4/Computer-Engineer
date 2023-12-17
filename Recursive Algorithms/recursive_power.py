def recursive_power(base, power, module) -> int:
    if power == 1:
        print(f'({base}^{power} % {module}) = {base ** power} % {module} = {base ** power % module}')
        return base % module
    elif power % 2 == 0:
        print(f'({base}^{power} % {module}) = ({base}^{power // 2} % {module})^2')
        temp = recursive_power(base, power // 2, module)
        return temp ** 2 % module
    elif power % 2 == 1:
        print(f'({base}^{power} % {module}) = ([{base} x {base}^{power - 1}] % {module})')
        temp = recursive_power(base, power - 1, module)
        return (base * temp) % module


x = int(input('Enter your base number (x ** n % p) --> x: '))
n = int(input('Enter your power number (x ** n % p) --> n: '))
p = int(input('Enter your module number (x ** n % p) --> p: '))
print(f'Remainder is: {recursive_power(x, n, p)}')

# print(f'Remainder is: {recursive_power(3, 50000000, 13)}')
