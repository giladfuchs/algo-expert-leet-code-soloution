def minNumberOfJumps(array):
    n = len(array)-1
    i, curr_max, max_till_now, count = (0,)*4
    while i<=curr_max and i<n:
        max_till_now = max(array[i] +i, max_till_now)
        if i == curr_max:
            curr_max = max_till_now
            count+=1
        i+=1
    return count

    return count
print(minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]))
