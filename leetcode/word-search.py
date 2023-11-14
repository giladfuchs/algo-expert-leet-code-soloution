from collections import  Counter
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if Solution.is_missing_chars(board, word):
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if Solution.rec_dfs(board, word, i=i, j=j):
                    return True

        return False

    @staticmethod
    def rec_dfs(board, word, S=None, i=0, j=0, index=0):
        current_char = board[i][j]
        if index >= len(word) or current_char != word[index]:
            return False
        elif index == len(word) - 1:
            return True

        if S is None: S = set();
        S.add((i, j))
        for k, l in Solution.get_neighbours(board, i, j):
            next_cur = board[k][l]
            if (k, l) in S: continue
            if Solution.rec_dfs(board, word, set(S), k, l, index + 1):
                return True
        return False

    @staticmethod
    def get_neighbours(matrix, i, j):
        N = []
        if i + 1 < len(matrix):
            N.append((i + 1, j))
        if i - 1 >= 0:
            N.append((i - 1, j))
        if j - 1 >= 0:
            N.append((i, j - 1))
        if j + 1 < len(matrix[0]):
            N.append((i, j + 1))
        return N

    # This trivial check improves the result to beat 90.66% of the results
    # Regarding running time
    @classmethod
    def is_missing_chars(cls, board, word):
        x = sum(board, [])
        if Counter(word) - Counter(x):
            return True
        return False


print(Solution().exist([["a","b"],["c","d"]], "cdba"))
print(Solution().exist([["a","b"],["c","d"]], "cdba"))
# print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
# print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))
