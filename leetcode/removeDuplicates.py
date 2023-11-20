from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = sorted(list(set(nums)))
        for i, num in enumerate(s):
            nums[i] = num

        return len(s)

    def removeDuplicatesNoSet(self, nums: List[int]) -> int:
        count = 1
        for i in range(len(nums)):
            if nums[i] != nums[i - 1]:
                nums[count] = nums[i]
                count += 1

        return count

    def removeDuplicates2(self, nums: List[int]) -> int:
        count, i = 0, 0
        while i < len(nums):
            j = i + 1
            while j < len(nums) and nums[i] == nums[j]:
                j += 1

            add_count = min([j - i, 2])
            for temp in range(add_count):
                nums[count + temp] = nums[i]
            # i = max(j - 1, i + 1)
            i = j
            count += add_count

        return count


# print(Solution().removeDuplicates([1, 1, 2]))
print(Solution().removeDuplicates2([1, 1, 1, 2, 2, 3]))
