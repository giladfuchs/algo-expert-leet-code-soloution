def maxProfit(prices) -> int:
    temp_min = prices[0]
    ans = 0

    for price in prices[1:]:
        if price - temp_min > ans:
            ans = price - temp_min
        if price< temp_min:
            temp_min = price
    return ans
from typing import List


class Solution:
    def maxProfit_easy(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_sell = 0
        for price in prices[1:]:
            if price - min_buy > max_sell:
                max_sell = price - min_buy
            if price < min_buy:
                min_buy = price
        return max_sell

    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        total = 0
        for i in range(len(prices) - 1):
            if prices[i] > prices[i + 1]:
                total += prices[i] - buy
                buy = prices[i + 1]

        total += prices[-1] - buy

        return total


if __name__ == '__main__':
    print(Solution().maxProfit([7, 2, 5, 3, 6, 1, 4]))
