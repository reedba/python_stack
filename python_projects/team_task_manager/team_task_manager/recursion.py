def recursionsum(x):
    if x <= 0:
        return 0
    return x + recursionsum(x-1)