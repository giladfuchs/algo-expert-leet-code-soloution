def zeroSumSubarray(nums: list):
    if not nums:
        return False
    if 0 in nums:
        return True
    left = [0] * len(nums)
    left[0] = nums[0]

    for i in range(len(left) - 1):
        left[i + 1] = left[i] + nums[i + 1]

    ls_sums = list(set(left))
    return 0 in ls_sums or len(ls_sums) != len(nums)
    # Write your code here.
    # return False


#
nums = [-5, -5, 2, 3, -2]
print(zeroSumSubarray([2, -2]))
# right = [0 ]* len(nums)
# nums2 = nums[::-1]
#
# right[0]=nums2[0]
# for i in range(len(left) - 1):
#     right[i + 1] = right[i] + nums2[i + 1]
# right = right[::-1]
#
# print(left)
# print(right)
