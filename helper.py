def is_power2(num):
    """states if a number is a power of two"""
    return num != 0 and ((num & (num - 1)) == 0)


def divisors(n):
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            yield i
    yield n
