def sortStack(stack: list):
    if len(stack) <= 1:
        return stack

    first = stack.pop()
    sortStack(stack)
    second = stack.pop()

    smaller = min(first, second)
    bigger = max(first, second)

    stack.append(smaller)
    sortStack(stack)
    stack.append(bigger)

    return stack


print(sortStack([-5, 2, -2, 4, 3, 1]))
