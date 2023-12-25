from typing import List

from collections import defaultdict

class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n <= 1:
            return 0
        return n // 2 + self.numberOfMatches((n + 1) // 2)

    def minSwaps(self, nums: List[int]) -> int:
        ones = nums.count(1)
        nums = nums + nums
        x = ones_window = 0
        for i in range(len(nums)):
            if i >= ones and nums[i - ones] == 1: x -= 1
            if nums[i] == 1: x += 1
            ones_window = max(ones_window, x)
        return ones - ones_window

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        size = len(nums) - 1
        for i in range(size + 1):
            if nums[i] > 0:
                break
            if i and nums[i] == nums[i - 1]:
                continue
            k = size
            j = i + 1
            while j < k:
                if k < size and nums[k] == nums[k + 1]:
                    k -= 1
                    continue
                temp = nums[i] + nums[j] + nums[k]
                if temp > 0:
                    k -= 1
                elif temp < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1

        return res


    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        count = 0
        for num in nums:
            if num - 1 not in s:

                i = 1
                while (num + i) in s:
                    i += 1

                count = max(count, i)
        return count
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for st in strs:
            d[sorted(st)].append(st)
        return list(d.values())

# print(Solution().numberOfMatches(7))
print(Solution().minSwaps([0, 1, 0, 1, 1, 0, 0]))
