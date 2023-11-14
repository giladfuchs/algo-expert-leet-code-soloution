from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        return self.merge(intervals)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []
        while intervals:
            start, end = intervals.pop(0)
            while intervals and end >= intervals[0][0]:
                end = max(intervals.pop(0)[1], end)
            ans.append((start, end))
        return ans

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key=lambda x: x[0], reverse=True)

        ans = [intervals[0]]
        for start, end in intervals[1:]:
            if ans[-1][0] >= end:
                ans.append([start, end])
            else:
                count += 1
        return count


# print(Solution().merge([[1, 4], [2, 3]]))
# print(Solution().insert([[1, 3], [6, 9]], [2, 5]))
# print(Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
print(Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
