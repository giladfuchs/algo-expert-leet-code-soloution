import math
from typing import List


class Solution:
    def getSumAbsoluteDifferences2(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            temp = 0
            for j in range(len(nums)):
                temp += abs(num - nums[j])

            res.append(temp)

        return res

    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sums_start = [nums[0]]
        for i in range(1, n):
            sums_start.append(sums_start[-1] + nums[i])
        sums_end = [nums[-1]]
        for i in range(len(nums) - 2, -1, -1):
            sums_end.append(sums_end[-1] + nums[i])
        sums_end = sums_end[::-1]
        res = [(i * nums[i] - sums_start[i] + (sums_end[i] - nums[i] * (n - i - 1))) for i in range(n)]
        return res

    def getSumAbsoluteDifferences3(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        prefix_sum = [0] * n
        suffix_sum = [0] * n

        # Calculate and initialize the prefix sums & suffix_sum array
        prefix_sum[0] = nums[0]
        suffix_sum[n - 1] = nums[n - 1]

        # Calculate the prefix sums & suffix_sum array in one loop
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
            suffix_sum[n - i - 1] = suffix_sum[n - i] + nums[n - i - 1]

        print()


# print(Solution().getSumAbsoluteDifferences2([2, 3, 5]))
# print(Solution().getSumAbsoluteDifferences([2, 3, 5]))
print(Solution().getSumAbsoluteDifferences2([1, 4, 6, 8, 10]))
# print(Solution().getSumAbsoluteDifferences([1, 4, 6, 8, 10]))
