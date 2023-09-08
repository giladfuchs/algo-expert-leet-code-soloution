def isMonotonic(array):
    size = len(array)
    down, up = True, True
    if size<2:
        return True
    i =1
    while (down or up) and i< size:
        up = up and array[i]>= array[i-1]
        down = down and array[i] <= array[i-1]
        i+=1
    return down or up

print(isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))