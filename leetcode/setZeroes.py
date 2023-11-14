import pprint
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        cords = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[i])) if matrix[i][j] == 0]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    cords.append((i, j))

        for i, j in cords:
            temp_i, temp_j = i - 1, j
            while temp_i > -1:
                matrix[temp_i][temp_j] = 0
                temp_i -= 1
            temp_i = i + 1
            while temp_i < len(matrix):
                matrix[temp_i][temp_j] = 0
                temp_i += 1
            temp_i = i
            temp_j -= 1
            while temp_j > -1:
                matrix[temp_i][temp_j] = 0
                temp_j -= 1
            temp_j = j + 1
            while temp_j < len(matrix[0]):
                matrix[temp_i][temp_j] = 0
                temp_j += 1

        pprint.pprint(matrix)



# print(Solution().setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
