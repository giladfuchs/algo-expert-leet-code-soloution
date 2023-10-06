def blackjackProbability(target, startingHand, ):
    prob = 0.1

    def helper(num, cache):
        if num in cache:
            return cache[num]
        if num > target:
            return 1
        if target - 4 <= num <= target:
            return 0

        res = prob * sum((helper(i, cache) for i in range(num + 1, num + 11)))
        cache[num] = round(res, 3)
        return cache[num]

    _cache = {}
    return helper(startingHand, _cache)


if __name__ == '__main__':
    print(blackjackProbability(10, 3))
