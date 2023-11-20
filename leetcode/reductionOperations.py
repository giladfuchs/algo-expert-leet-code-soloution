from typing import List


class Solution:
    # cheat solution
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort( )
        n = len(nums)
        i = n - 1
        count = 0

        while i > 0:
            if nums[i] != nums[i - 1]:
                count += (n - i)
            i -= 1
        return count
    # my Solution
    def reductionOperationsMy(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        i = 0
        n = len(nums)
        count_add = len(set(nums)) - 1
        count = 0

        while i < n - 1:
            if nums[i] != nums[i + 1]:
                count += count_add
                count_add -= 1
            elif nums[i] != nums[-1]:
                count += count_add

            i += 1
        return count


print(Solution().reductionOperations([1, 1, 2, 2, 3]))
print(Solution().reductionOperations([5, 1, 3]))
