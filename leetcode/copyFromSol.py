import heapq
from typing import List
from collections import Counter


class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]
            cur_max, res = 0, 0
            for j in range(i, min(len(arr), i + k)):
                cur_max = max(cur_max, arr[j])
                size = j - i + 1
                res = max(res, dfs(j + 1) + cur_max * size)
            cache[i] = res
            return res

        return dfs(0)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        total = n + m
        half = total // 2
        if m < n:
            n, m = m, n
            nums1, nums2 = nums2, nums1
        left, right = 0, n - 1

        while True:
            i = (left + right) // 2
            j = half - i - 2
            aLeft = nums1[i] if i >= 0 else float("-inf")
            aRight = nums1[i + 1] if i + 1 < n else float("inf")
            bLeft = nums2[j] if j >= 0 else float("-inf")
            bRight = nums2[j + 1] if j + 1 < m else float("inf")

            if aLeft <= bRight and bLeft <= aRight:
                if total % 2 != 0:
                    return min(aRight, bRight)
                return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            elif aLeft > bRight:
                right = i - 1
            else:
                left = i + 1

    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0
        for target in range(1, n + 1):
            for s in range(1, target + 1):
                squ = s * s
                if target - squ < 0:
                    break
                if dp[target - squ] + 1 < dp[target]:
                    dp[target] = dp[target - squ] + 1
        return dp[n]

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        for i in range(1, n):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, m):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]

    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        st = []
        for index, height in enumerate(heights):
            start = index
            while st and st[-1][1] > height:
                i, h = st.pop()
                res = max(res, (index - i) * h)
                start = i

            st.append((start, height))

        for i, h in st:
            res = max(res, (n - i) * h)
        return res

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        box = [[set() for i in range(3)] for i in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in box[i // 3][j // 3]:
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                box[i // 3][j // 3].add(board[i][j])

        return True

    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n

            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow

        return row[0]

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        n = len(heights) - 1
        for i in range(n):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue
            bricks -= diff
            heapq.heappush(heap, -diff)
            if bricks < 0:
                if ladders == 0:
                    return i
                ladders -= 1
                bricks += -heapq.heappop(heap)

        return n

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        vals = list(count.values())
        vals.sort()
        res = len(vals)
        i = 0
        while k > 0:
            k -= vals[i]
            i += 1
            if k >= 0:
                res -= 1

        return res

    def binary_search(self, nums, target, find_first):
        left, right = 0, len(nums) - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                result = mid

                if find_first:
                    right = mid - 1  # Search in the left half for the first occurrence
                else:
                    left = mid + 1  # Search in the right half for the last occurrence
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result

    def searchRange(self, nums, target):
        # Find the first and last occurrences of the target using binary search
        first_occurrence = self.binary_search(nums, target, True)
        last_occurrence = self.binary_search(nums, target, False)
        return [first_occurrence, last_occurrence]

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def get_pattern(word):
            start = 'a'
            seen = {}
            ans = ''
            for ch in word:
                if ch not in seen:
                    seen[ch] = start
                    start = chr(ord(start) + 1)
                ans += seen[ch]
            return ans

        res = []
        pattern = get_pattern(pattern)

        for word in words:
            if pattern == get_pattern(word):
                res.append(word)
        return res

    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []
        while i < len(firstList) and j < len(secondList):
            f_start, f_end = firstList[i]
            s_start, s_end = secondList[j]
            if f_start <= s_end and s_start <= f_end:
                res.append([max(f_start, s_start), min(f_end, s_end)])
            if f_end <= s_end:
                i += 1
            else:
                j += 1
        return res

    def countSubstrings(self, s, t):
        n, m = len(s), len(t)

        match = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        matchone = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    match[i][j] = 1 + match[i - 1][j - 1]
                    matchone[i][j] = matchone[i - 1][j - 1]
                else:
                    match[i][j] = 0
                    matchone[i][j] = 1 + match[i - 1][j - 1]

        return sum([sum(i) for i in matchone])


print(Solution().countSubstrings(s="aaab", t="aaac"))
# print(Solution().intervalIntersection(firstList=[[0, 2], [5, 10], [13, 23], [24, 25]],
#                                       secondList=[[1, 5], [8, 12], [15, 24], [25, 26]]))

# print(Solution().findAndReplacePattern(words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "cee"))
# print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
# print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
# print(Solution().findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3))

# print(Solution().maxSumAfterPartitioning(arr=[1, 15, 7, 9, 2, 5, 10], k=3))
# print(Solution().numSquares(12))
# print(Solution().uniquePaths(m=3, n=7))
