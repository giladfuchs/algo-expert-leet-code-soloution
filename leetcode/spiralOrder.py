from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        i, j = 0, 0
        path = []
        gap = 0

        while len(path) < m * n:
            while len(path) < m * n and j < m - gap:
                current_element = matrix[i][j]
                path.append(current_element)
                j += 1
            j -= 1
            i += 1
            while len(path) < m * n and i < n - gap:
                path.append(matrix[i][j])
                i += 1
            i -= 1
            j -= 1
            while len(path) < m * n and j >= gap:
                path.append(matrix[i][j])
                j -= 1
            j += 1
            i -= 1
            while len(path) < m * n and i >= 1 + gap:
                path.append(matrix[i][j])
                i -= 1
            i += 1
            j += 1
            gap += 1
        return path

 

# print(Solution().spiralOrder(matrix=[[3], [2]]))
# print(Solution().spiralOrder(matrix=[[1]]))
print(Solution().spiralOrder2(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution().spiralOrder(matrix=[[1, 2, 3, 4],
                                     [5, 6, 7, 8],
                                     [9, 10, 11, 12]]))
