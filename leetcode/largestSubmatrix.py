from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])

        # Calculate heights for each column
        for i in range(1, row):
            for j in range(col):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]

        res = 0
        for i in range(row):
            # Sort the heights in ascending order
            matrix[i].sort()

            # Iterate through the sorted heights
            ֿ
            for j in range(col):
                height = matrix[i][j]
                width = col - j
                res = max(res, height * width)

        return res

print(Solution().largestSubmatrix([[0,0,1],[1,1,1],[1,0,1]]))