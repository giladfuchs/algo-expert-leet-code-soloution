from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (r - l) // 2 + l
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]


print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))
print(Solution().findMin([3, 4, 5, 1, 2]))
print(Solution().findMin([11, 13, 15, 17]))
