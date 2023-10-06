def sortStack(stack: list):
    st_temp = []
    st_temp.append(stack.pop())

    while stack:
        if st_temp[-1] <= stack[-1]:
            st_temp.append(stack.pop())
        else:
            stack.append(st_temp.pop())

    return []
