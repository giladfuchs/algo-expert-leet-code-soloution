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
        # Initialize reach (maximum reachable index), count (number of jumps), and last (rightmost index reached)
        reach, count, last = 0, 0, 0

        # Loop through the array excluding the last element
        for i in range(len(nums) - 1):
            # Update reach to the maximum between reach and i + nums[i]
            reach = max(reach, i + nums[i])

            # If i has reached the last index that can be reached with the current number of jumps
            if i == last:
                # Update last to the new maximum reachable index
                last = reach
                # Increment the number of jumps made so far
                count += 1

        # Return the minimum number of jumps required
        return count



def knightConnection(knightA, knightB):
    # src = (src // 8, src % 8)
    # dest = (dest // 8, dest % 8)

    q = deque([(knightA[0], knightA[1], 0)])
    visited = {(knightA[0], knightA[1])}

    while True:
        current = q.popleft()
        if current[0] == knightB[0] and current[1] == knightB[1]:
            return math.ceil(current[2]/2)
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
