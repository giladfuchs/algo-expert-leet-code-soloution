from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        to_add = []
        def dfs(i):
            if i>=len(nums):
                res.append(to_add.copy())
                return
            to_add.append(nums[i])
            dfs(i+1)
            to_add.pop()
            dfs(i+1)
        dfs(0)

        return res

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return

                # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            # All subsets that don't include nums[i]
            # while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            #     i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])

        return res

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def permute_help(l, r):
            if l == r:
                res.append(nums.copy())
            else:
                for i in range(l, r):
                    nums[l], nums[i] = nums[i], nums[l]
                    permute_help(l + 1, r)
                    nums[l], nums[i] = nums[i], nums[l]

        permute_help(0, len(nums))
        return res
print(Solution().permute([1,2,3]))