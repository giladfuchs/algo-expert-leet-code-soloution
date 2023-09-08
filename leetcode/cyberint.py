num = 7
def foo(c):
    yield f'{c}$'
b = foo('aaa')
print(b.__next__())
def dec(func):
    def inn(c):
        func(c)
        return f'{c}$'
    return inn
@dec
def funcc(c):
    print(c)
    return c
print(funcc('dd'))
a = [f'{i}$' for i in range(num+1)]
# 7 __eq__

# @
# def foo(x):
#     def