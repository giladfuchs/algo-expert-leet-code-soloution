from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1
        while start <= end:
            med = (end - start) // 2 + start
            if matrix[med][0] <= target and  matrix[med][-1] >= target:
                break
            if matrix[med][0] <= target:
                start = med + 1
            else:
                end = med
        if start>end:
            return False

        arr = matrix[med]
        start = 0
        end = len(arr) - 1
        while start <= end:
            med = (end - start) // 2 + start
            if arr[med] == target :
                return True
            if arr[med] < target:
                start = med + 1
            else:
                end = med
        return False

Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 32)