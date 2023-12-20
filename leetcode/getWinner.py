from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner = arr[0]
        wins = 0
        for i in range(1, len(arr)):
            if arr[i] < winner:
                wins += 1
            else:
                winner = arr[i]
                wins = 1
            if wins == k:
                return winner
        return winner

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        mat = [[] for _ in range(m)]
        for j in range(m):
            for i in range(n):
                mat[j].append(matrix[i][j])
        return mat



print(Solution().transpose([[1, 2, 3], [4, 5, 6], ]))
