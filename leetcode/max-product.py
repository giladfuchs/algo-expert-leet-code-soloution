def maxProuductHelp(nums):
    max_sum = nums[0]
    temp_sum = 1

    for num in nums:
        temp_sum *= num
        if temp_sum > max_sum:
            max_sum = temp_sum
        if temp_sum == 0:
            temp_sum = 1
    return max_sum

def maxProuduct(nums):

    return max(maxProuductHelp(nums), maxProuductHelp(nums[::-1]))


if __name__ == '__main__':
    print(maxProuduct([2,-5,-2,-4,3]))
    print(maxProuduct([-2,0,-1]))
