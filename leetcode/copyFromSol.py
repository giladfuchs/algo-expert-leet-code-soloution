from typing import List


class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]
            cur_max, res = 0, 0
            for j in range(i, min(len(arr), i + k)):
                cur_max = max(cur_max, arr[j])
                size = j - i + 1
                res = max(res, dfs(j + 1) + cur_max * size)
            cache[i] = res
            return res

        return dfs(0)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        total = n + m
        half = total // 2
        if m < n:
            n, m = m, n
            nums1, nums2 = nums2, nums1
        left, right = 0, n - 1

        while True:
            i = (left + right) // 2
            j = half - i - 2
            aLeft = nums1[i] if i >= 0 else float("-inf")
            aRight = nums1[i + 1] if i + 1 < n else float("inf")
            bLeft = nums2[j] if j >= 0 else float("-inf")
            bRight = nums2[j + 1] if j + 1 < m else float("inf")

            if aLeft <= bRight and bLeft <= aRight:
                if total % 2 != 0:
                    return min(aRight, bRight)
                return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            elif aLeft > bRight:
                right = i - 1
            else:
                left = i + 1

    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0
        for target in range(1, n + 1):
            for s in range(1, target + 1):
                squ = s * s
                if target - squ < 0:
                    break
                if dp[target - squ] + 1 < dp[target]:
                    dp[target] = dp[target - squ] + 1
        return dp[n]


# print(Solution().maxSumAfterPartitioning(arr=[1, 15, 7, 9, 2, 5, 10], k=3))
# print(Solution().numSquares(12))
