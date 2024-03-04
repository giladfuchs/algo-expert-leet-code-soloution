from typing import List

from collections import Counter, deque, defaultdict


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_row = [max(row) for row in grid]
        max_col = [max(col) for col in zip(*grid)]
        ans = 0
        for i in range(len(max_row)):
            for j in range(len(max_col)):
                ans += min(max_row[i], max_col[j]) - grid[i][j]

        return ans

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        i, j, count, ans = 0, 0, 0, len(nums)
        while j < len(nums):
            count += nums[j]
            j += 1
            while count >= target:
                ans = min(ans, j - i)
                count -= nums[i]
                i += 1
        return ans

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                if i - d[nums[i]] <= k:
                    return True
            d[nums[i]] = i
        return False


print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
# print(Solution().maxIncreaseKeepingSkyline([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]))
