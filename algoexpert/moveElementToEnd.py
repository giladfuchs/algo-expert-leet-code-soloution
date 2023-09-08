def moveElementToEnd(array, toMove):
    size = len(array)
    end = size-1
    start = 0
    while start<end:
        while  start<end and array[end] == toMove:
            end-=1
        if array[start] == toMove:
            array[start], array[end] = array[end], array[start]

        start+=1

    return array

print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2],2))
