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

    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        qua = n // 4

        def helpFindSpecialInteger(index: int) -> int:
            i = index + 1
            while i < n and arr[i] == arr[index]: i += 1

            count = i - index - 1
            i = index - 1
            while i > -1 and arr[i] == arr[index]: i -= 1
            count += index + (- i if i > 0 else 0)
            return count

        if arr[0] == arr[qua] or arr[qua] == arr[n // 2]:
            return arr[qua]

        if arr[n // 2 + qua] == arr[n // 2]:
            return arr[n // 2]

        for i in range(qua, n, qua):
            if helpFindSpecialInteger(i) > qua:
                return arr[i]
        return arr[-1]

    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        for row in mat:
            if sum(row) == 1:
                i = row.index(1)
                if sum(row2[i] for row2 in mat) == 1:
                    count += 1

        return count


print(Solution().numSpecial([[1, 0, 0], [0, 0, 1], [1, 0, 0]]
                            ))
# print(Solution().findSpecialInteger([0,1,1,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5,5,5]
# ))
# print(Solution().spiralOrder(matrix=[[3], [2]]))
# print(Solution().spiralOrder(matrix=[[1]]))
# print(Solution().spiralOrder2(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(Solution().spiralOrder(matrix=[[1, 2, 3, 4],
#                                      [5, 6, 7, 8],
#                                      [9, 10, 11, 12]]))
