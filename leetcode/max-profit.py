def maxProfit(prices) -> int:
    temp_min = prices[0]
    ans = 0

    for price in prices[1:]:
        if price - temp_min > ans:
            ans = price - temp_min
        if price< temp_min:
            temp_min = price
    return ans


if __name__ == '__main__':
    print(maxProfit([7, 1, 5, 3, 6, 4]))
