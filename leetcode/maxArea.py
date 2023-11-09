from typing import List


class Solution:
    def maxAreaN2(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                temp_area = min(height[i], height[j]) * (j - i)
                if temp_area > max_area:
                    max_area = temp_area
        return max_area

    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = min(height[left], height[right]) * (right - left)

        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            temp_area = min(height[left], height[right]) * (right - left)
            if temp_area > max_area:
                max_area = temp_area

        return max_area


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
