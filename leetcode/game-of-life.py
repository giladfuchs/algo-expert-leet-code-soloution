import functools
from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        n = len(board)
        m = len(board[0])

        def check_cell(board: List[List[int]], i, j) -> int:
            count = 0
            for x in range(max([0, i - 1]), min([i + 1, n - 1]) + 1):
                for y in range(max([0, j - 1]), min([j + 1, m - 1]) + 1):
                    if board[x][y] and not (x == i and j == y):
                        count += 1

            if board[i][j]:
                if count < 2:
                    return 0
                if count < 4:
                    return 1
                return 0

            return 1 if count == 3 else 0
        ans = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j]= check_cell(board, i, j)
        board = [list(_) for _ in ans]
        print(board)
def solution(inputArray):
    d  = functools.reduce(lambda x, y: {**x, len(y): x.get(len(y), []) + [y]}, inputArray, {})
    return d[max(list(d.keys()))]
print(solution(["aba",
 "aa",
 "ad",
 "vcd",
 "aba"]))
# Solution().gameOfLife(board =[[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
# Solution().gameOfLife(board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]])