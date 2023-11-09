class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        return not (sx == fx and sy == fy and t == 1) and t >= max(abs(sx - fx), abs(sy - fy))


# print(Solution().isReachableAtTime(sx=2, sy=4, fx=7, fy=7, t=6))
print(Solution().isReachableAtTime(sx=1, sy=2, fx=1, fy=2, t=1))
