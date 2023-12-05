from typing import List



class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums)
        nums.insert(0, float('-inf'))
        nums.append(float('-inf'))
        while start < end:
            mid = (end - start) // 2 + start
            if nums[mid + 1] < nums[mid] > nums[mid - 1]:
                return mid - 1
            elif nums[mid] < nums[mid + 1]:
                start = mid + 1
            else:
                end = mid

        return mid + 1


print(Solution().findPeakElement([1, 2, 3, 1]))
