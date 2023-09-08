def waterArea(heights):
    if not heights:
        return 0
    max_num = heights[0]
    max_index = 0
    end = len(heights)-1
    count=0
    first=False
    for i in range(1, end):
        if heights[i]>=max_num:
            if not first:
                first=True
                max_index = i
            else:
                max_index += 1
                while max_index< i:
                    count+= max_num - heights[max_index]
                    max_index+=1
            max_num = heights[i]

    max_index+=1
    while max_index< end:
        count+= min(max_num, heights[end]) - heights[max_index]
        max_index+=1

    return count
# print(waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))
print(waterArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))