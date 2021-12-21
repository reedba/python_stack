def recursionsum(x):
    if x <= 0:
        return 0
    return x + recursionsum(x-1)


result1 = recursionsum(5)

print(result1)


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

result = factorial(5)

print(result)