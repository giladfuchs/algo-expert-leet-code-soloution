import math
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        reachable = 0

        for i in range(len(nums)):

            if i > reachable:
                return False

            reachable = max(reachable, i + nums[i])
            if reachable >= len(nums):
                return True
        return True

    def jump(self, nums):
        reach, count, last = 0, 0, 0

        for i in range(len(nums) - 1):
            reach = max(reach, i + nums[i])

            if i == last:
                last = reach
                count += 1

        return count

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1


def knightConnection(knightA, knightB):
    # src = (src // 8, src % 8)
    # dest = (dest // 8, dest % 8)

    q = deque([(knightA[0], knightA[1], 0)])
    visited = {(knightA[0], knightA[1])}

    while True:
        current = q.popleft()
        if current[0] == knightB[0] and current[1] == knightB[1]:
            return math.ceil(current[2] / 2)
        for x, y in get_paths((current[0], current[1])):
            if (x, y) not in visited:
                q.append((x, y, current[2] + 1))
                visited.add((x, y))

# knightConnection([10, 10], [-10, -10])

# 1+ 2 + 3
# 1 + 2 + 2+1
# if __name__ == '__main__':
# foo(" '--->-><-><-->-'")
# print(Solution().canJump([2, 3, 1, 1, 4]))
# print(Solution().canJump([2, 3, 1, 1, 4]))
# print(Solution().canJump([3, 2, 1, 0, 4]))
