def outer(func):
    def inner(n):
        n= n * 4
        return func(n)

    return inner
@outer
def a(n):
    print(n)
    return n*3
print(a(5))
