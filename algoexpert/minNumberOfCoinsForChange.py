from typing import Union, List


def minNumberOfCoinsForChange(n, denoms):
    num_coins: List[Union[int, float]] = [0] + [float('inf') for _ in range(n)]
    for d in denoms:
        for amount in range(d, n + 1):
            print(num_coins[amount], num_coins[amount - d])
            num_coins[amount] = min(num_coins[amount], num_coins[amount - d] + 1)
    res = num_coins[n]
    return res if res != float('inf') else -1


minNumberOfCoinsForChange(7, [1, 5, 10])
