from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        max_area = 0
        start, _ = points.pop(0)
        for x, _ in points:
            max_area = max(max_area, x - start)
            start = x
        return max_area


# print(Solution().maxWidthOfVerticalArea([[8, 7], [9, 9], [7, 4], [9, 7]]))
# print(Solution().maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))
print(Solution().maxWidthOfVerticalArea([[2, 4], [10, 10], [6, 9], [6, 8], [6, 10], [8, 6], [5, 3]]

                                        ))
