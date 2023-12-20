from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        counter = [0] + [float('inf')] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                counter[i] = min(counter[i - coin] + 1, counter[i])

        return counter[-1] if counter[-1] != float('inf') else -1

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans = 0
        for i in range(len(piles) // 3, len(piles), 2):
            ans += piles[i]
        # while piles:
        #     piles.pop()
        #     ans += piles.pop()
        #     piles.pop(0)

        return ans

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        return True

    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
        return ""


print(Solution().largestOddNumber("52"))
# print(Solution().canFinish(prerequisites=[[1, 0], [0, 1]], numCourses=2))
# print(Solution().coinChange(coins=[1, 2, 5], amount=11))
