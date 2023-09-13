from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        counter = [0] + [float('inf')] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                counter[i] = min(counter[i - coin] + 1, counter[i])

        return counter[-1]


print(Solution().coinChange(coins=[1, 2, 5], amount=11))
