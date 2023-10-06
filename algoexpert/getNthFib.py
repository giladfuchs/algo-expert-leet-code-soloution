def fib(n):
    if n < 2:
        return n

    if n % 2 == 0:
        return (2 * fib(n // 2 - 1) + fib(n // 2)) * fib(n // 2)
    else:
        return fib((n + 1) // 2 - 1) * fib((n + 1) // 2 - 1) + fib((n + 1) // 2) * fib((n + 1) // 2)


def getNthFib(n):
    return fib(n + 1)


print(getNthFib(3))
