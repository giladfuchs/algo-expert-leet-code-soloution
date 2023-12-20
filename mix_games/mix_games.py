def deco(func):
    def inner(val):
        func(val * val)

    return inner


def gene(num):
    yield num * num


@deco
def foo(j):
    print(j)


foo(3)
print(next(gene(5)))
