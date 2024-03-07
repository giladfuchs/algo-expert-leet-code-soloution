from typing import List

from collections import Counter, deque, defaultdict
from sortedcontainers import SortedList


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

    def minimumLength(self, s: str) -> int:
        ls = list(s)
        while len(ls) > 1:
            start, end = 0, len(ls) - 1
            if ls[start] == ls[end]:
                ch = ls[0]
                while start < end and ls[start] == ch:
                    start += 1
                while end > 0 and ls[end] == ch:
                    end -= 1
                ls = ls[start:end + 1] if start <= end else []
            else:
                break

        return len(ls)

    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        ans = 0
        while tokens:
            if tokens[0] <= power:
                ans += 1
                power -= tokens.pop(0)
            elif len(tokens) > 1 and ans > 0:
                ans -= 1
                power += tokens.pop()
            else:
                break

        return ans

    def combine(self, n: int, k: int) -> List[List[int]]:
        data = [0] * k
        arr = list(range(1, n + 1))
        ans = []

        def combinationUtil(index, i):

            if (index == k):
                ans.append(data[:])
                return

            if (i >= n):
                return

            data[index] = arr[i]
            combinationUtil(index + 1, i + 1)

            combinationUtil(index, i + 1)

        combinationUtil(0, 0)
        return ans

    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        vals = SortedList()
        ans = float('inf')
        for i, v in enumerate(nums):
            if i >= x:
                vals.add(nums[i - x])
                k = vals.bisect_left(v)
                if k:
                    ans = min(ans, v - vals[k - 1])
                if k < len(vals):
                    ans = min(ans, vals[k] - v)
        return ans

    def maxSum(self, nums: List[int]) -> int:
        ans = -1
        max_dict = {}
        for num in nums:
            max_digit = max([int(digit) for digit in str(num)])
            if max_digit in max_dict:
                ans = max(ans, num + max_dict[max_digit])
                max_dict[max_digit] = max(max_dict[max_digit], num)
            else:
                max_dict[max_digit] = num

        return ans


# print(Solution().bagOfTokensScore(tokens=[100], power=50))
# print(Solution().bagOfTokensScore(tokens=[200, 100], power=150))
# print(Solution().bagOfTokensScore(tokens=[100, 200, 300, 400], power=200))
# print(Solution().minimumLength("cabaabac"))
# print(Solution().minAbsoluteDifference(nums=[4, 3, 2, 4], x=2))
print(Solution().minAbsoluteDifference(nums=[5, 3, 2, 10, 15], x=1))
# print(Solution().combine(4, 2))
# print(Solution().minimumLength("aabccabba"))
# print(Solution().minimumLength("bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"))
# print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
# print(Solution().maxIncreaseKeepingSkyline([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]))
