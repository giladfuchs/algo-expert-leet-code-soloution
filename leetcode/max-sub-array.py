def maxSubArray(nums):
    max_sum = nums[0]
    temp_sum = 0

    for num in nums:
        temp_sum += num
        if temp_sum > max_sum:
            max_sum = temp_sum
        if temp_sum < 0:
            temp_sum = 0
    return max_sum


if __name__ == '__main__':
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(maxSubArray([5,4,-1,7,8]))
