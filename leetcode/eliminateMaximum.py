import math
from typing import List
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        count_round = [math.ceil(dist[i] / speed[i]) for i in range(len(speed))]
        count_round.sort()
        for i, num in enumerate(count_round):
            if i >= num:
                return i or 1

        return len(speed)


print(Solution().eliminateMaximum(dist=[3, 5, 7, 4, 5], speed=[2, 3, 6, 3, 2]))
print(Solution().eliminateMaximum(dist=[1, 3, 4], speed=[1, 1, 1]))
print(Solution().eliminateMaximum(dist=[1, 1, 2, 3], speed=[1, 1, 1, 1]))
print(Solution().eliminateMaximum(dist=[3, 2, 4], speed=[5, 3, 2]))
