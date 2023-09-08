# from algoexpert.binarySearch import binarySearchLower


def sweetAndSavoryold(dishes, target):
    dishes.sort()
    print(dishes)
    # Write your code here.
    savor, sweet = 0, len(dishes) - 1
    # temp = dishes[savor] + dishes[sweet]
    while savor < sweet:
        temp = target + (dishes[savor] + dishes[sweet])
        right = target + (dishes[savor + 1] + dishes[sweet])
        left = target + (dishes[savor] + dishes[sweet - 1])
        if right < temp and left < temp:

            if left < right:
                savor += 1
            else:
                sweet -= 1

        else:
            if right < temp:
                savor += 1
            elif left < temp:
                sweet -= 1
            else:
                return [dishes[savor], dishes[sweet]]
    return [dishes[savor], dishes[sweet]]

def binarySearchLower(array, target):
    start, end = 0, len(array)-1

    ans = 0
    while start < end :
        mid = (end - start) // 2 + start
        if array[mid] >= target:
            end = mid-1
        else:
            start = mid + 1
            ans = mid+1
    return array[ans ]

def sweetAndSavory(dishes, target):
    dishes.sort()

    # Write your code here.
    sweets = [_ for _ in dishes if _ > 0]
    savors = [_ for _ in dishes if _ < 0]
    best_temp = float('inf')
    ans = [0, 0]
    for savor in savors:
        temp = target - savor
        sweet = binarySearchLower(sweets, temp)
        if (target >= 0 and abs(target - (savor + sweet)) <= abs(target - best_temp)) or target + (
                savor + sweet) <= target + best_temp:
            best_temp = savor + sweet
            ans = [savor, sweet]

    return ans if best_temp <= target else [0, 0]
    # print(best_temp)
    # print(sweets, savors)


if __name__ == '__main__':
    print(sweetAndSavory([-3, -5, 1, 7], 8))
    print(sweetAndSavory([-3, -5, 1, 7], 0))
    print(sweetAndSavory([5, -10], -4))
