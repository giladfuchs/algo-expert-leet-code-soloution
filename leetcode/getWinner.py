from typing import List
from collections import Counter


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner = arr[0]
        wins = 0
        for i in range(1, len(arr)):
            if arr[i] < winner:
                wins += 1
            else:
                winner = arr[i]
                wins = 1
            if wins == k:
                return winner
        return winner

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        mat = [[] for _ in range(m)]
        for j in range(m):
            for i in range(n):
                mat[j].append(matrix[i][j])
        return mat

    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [-1] * n
        right = [n] * n
        stack = []

        for i, value in enumerate(arr):
            while stack and arr[stack[-1]] >= value:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack = []

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        mod = 10 ** 9 + 7
        res = 0
        for i, value in enumerate(arr):
            temp = (i - left[i]) * (right[i] - i) * value
            res += temp
            # result = sum((i - left[i]) * (right[i] - i) * value for i, value in enumerate(arr)) % mod

        return res

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        odd, even = nums[1], nums[0]
        for i in range(2, len(nums)):
            if i % 2 == 0:
                odd = max(odd, even)
                even += nums[i]
            else:
                even = max(odd, even)
                odd += nums[i]
        return max(odd, even)

    def robCircle(self, nums):
        def help(arr):
            if len(arr) == 1:
                return arr[0]
            odd, even = arr[1], arr[0]
            for i in range(2, len(arr)):
                if i % 2 == 0:
                    odd = max(odd, even)
                    even += arr[i]
                else:
                    even = max(odd, even)
                    odd += arr[i]
            return max(odd, even)

        if len(nums) == 1:
            return nums[0]
        return max(help(nums[1:]), help(nums[:-1]))

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = matrix.copy()
        for i in range(n - 1, 0, -1):
            for j in range(n):
                min_cell = matrix[i][j]
                if j > 0:
                    min_cell = min(min_cell, matrix[i][j - 1])
                if j < n - 1:
                    min_cell = min(min_cell, matrix[i][j + 1])
                dp[i - 1][j] += min_cell
        return min(dp[0])

    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]

        class LargerNumKey(str):
            def __lt__(x, y):
                return x + y > y + x

        nums.sort(key=LargerNumKey)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if f"{nums[j]}{nums[i]}" > f"{nums[i]}{nums[j]}":
        #             nums[i], nums[j] = nums[j], nums[i]
        ans = ''.join(nums)
        if int(ans) == 0:
            return '0'
        return ans

    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        n = len(nums) // 2
        for num, count in counter.items():
            if count > n:
                return num

    def majorityElement3(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        co1 = maj1 = maj2 = co2 = 0
        for num in nums:
            if co1 == 0 and num != maj2:
                co1 = 1
                maj1 = num
            elif co2 == 0 and num != maj1:
                co2 = 1
                maj2 = num
            elif maj1 == num:
                co1 += 1
            elif maj2 == num:
                co2 += 1
            else:
                co1 -= 1
                co2 -= 1
        res = []
        threshold = len(nums) // 3
        co1 = co2 = 0
        for num in nums:
            if num == maj1:
                co1 += 1
            elif num == maj2:
                co2 += 1
        if co1 > threshold:
            res.append(maj1)
        if co2 > threshold:
            res.append(maj2)
        return res
    # print(Solution().largestNumber([3, 30, 34, 5, 9]))


print(Solution().sumSubarrayMins([3,1,2,4]))
# print(Solution().majorityElement3([3,2,3]))
# print(Solution().rob([2, 1, 1, 2]))
# print(Solution().trailingZeroes(7))
# print(Solution().minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
# print(Solution().sumSubarrayMins([3, 1, 2, 4]))
# print(Solution().transpose([[1, 2, 3], [4, 5, 6], ]))
