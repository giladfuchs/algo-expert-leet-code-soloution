def minRewards(scores):
    n = len(scores)
    rewards = [1] * n
    def backtrack():
        for index in range(n - 1):
            if scores[index] < scores[index + 1]:
                rewards[index + 1] = max(rewards[index] + 1, rewards[index + 1])

    backtrack()
    rewards = rewards[::-1]
    scores = scores[::-1]
    backtrack()
    return sum(rewards)


print(minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]))
# print(minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5][::-1]))