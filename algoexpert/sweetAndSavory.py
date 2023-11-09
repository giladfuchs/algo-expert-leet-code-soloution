def sweetAndSavory(dishes, target):
    sweet = sorted([dish for dish in dishes if dish < 0])
    savory = sorted([dish for dish in dishes if dish > 0])
    ans = [0, 0]
    if not savory or not sweet:
        return ans
    point_savory = len(savory) - 1
    point_sweet = 0
    diff = float('inf')
    while point_sweet < len(sweet) and point_savory >= 0:
        temp = [sweet[point_sweet], savory[point_savory]]
        sum_temp = sum(temp)
        if sum_temp == target:
            return temp
        if sum_temp > target:
            point_savory -= 1
            continue
        if abs(target - sum_temp) <= abs(target - diff):
            ans = temp
            diff = sum_temp
        point_sweet += 1
    return ans


if __name__ == '__main__':
    print(sweetAndSavory([-3, -5, 1, 7], 0))  # [-7, 2]
    # print(sweetAndSavory([2, 5, -4, -7, 12, 100, -25], -5))  # [-7, 2]

    # print(sweetAndSavory([6,5,], 0))
    # print(sweetAndSavory([5,-4,-5], 0))
    # print(sweetAndSavory([-3, -5, 1, 7], 0))
    # print(sweetAndSavory([5, -10], -4))
    # print(sweetAndSavory([-3, -5, 1, 7], 0))
    # print(sweetAndSavory([3, 5, 7, 2, 6], 0))
    # print(sweetAndSavory([2, 5, -4, 7, 12, 100, -25], -20))
    # print(sweetAndSavory([5, -10], -4))
