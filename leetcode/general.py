from typing import List

from collections import Counter, deque, defaultdict


class Solution:
    def minOperations(self, s: str) -> int:
        size = len(s)
        count1, count2 = 0, 0

        for i in range(size):
            if i % 2 == 0:
                if s[i] != '1':
                    count1 += 1
            elif s[i] != '0':
                count1 += 1
        for i in range(size):
            if i % 2 == 0:
                if s[i] != '0':
                    count2 += 1
            elif s[i] != '1':
                count2 += 1
        return min(count1, count2)

    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        s = set([(x, y)])
        for way in path:
            if way == "N":
                x -= 1
            elif way == "S":
                x += 1
            elif way == "E":
                y += 1
            elif way == "W":
                y -= 1
            if (x, y) in s:
                return True
            s.add((x, y))
        return False

    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row1, col1, row0, col0 = [[] for _ in range(4)]
        for row in grid:
            row1.append(row.count(1))
            row0.append(row.count(0))
        for row in zip(*grid):
            col1.append(row.count(1))
            col0.append(row.count(0))
        ans = [[None for _ in range(len(col0))] for __ in range(len(row1))]
        for i in range(len(row1)):
            for j in range(len(col0)):
                ans[i][j] = row1[i] + col1[j] - row0[i] - col0[j]
        return ans

    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0

        prev, cur = 1, 1

        for i in range(2, len(s) + 1):
            one_digit = int(s[i - 1])
            two_digits = int(s[i - 2:i])
            temp = 0
            if one_digit != 0:
                temp += cur

            if 10 <= two_digits <= 26:
                temp += prev

            prev, cur = cur, temp

        return cur

    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i, count = 0, 0
        n = len(colors)
        while i < n - 1:
            if colors[i] != colors[i + 1]:
                i += 1
            else:
                j = i + 1
                while j < n - 1 and colors[j] == colors[j + 1]: j += 1
                temp = neededTime[i:j + 1]
                count += sum(temp) - max(temp)
                i = j
        return count

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10 ** 9 + 7

        if n * k < target:
            return 0

        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(i, min(i * k, target) + 1):
                for temp in range(1, min(k, j) + 1):
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - temp]) % mod

        return int(dp[n][target])

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        maxi = -1
        d = {}
        for i, ch in enumerate(s):
            if ch in d:
                maxi = max(maxi, i - d[ch] - 1)
            else:
                d[ch] = i
        return maxi
        # print(Solution().minCost(colors="abaac", neededTime=[1, 2, 3, 4, 5]))

    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        counter = Counter(list(''.join(words)))
        for val in counter.values():
            if val % n != 0:
                return False
        return True

    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 1
        while i < n:
            count = 1
            while i < n and chars[i] == chars[i - 1]:
                chars.pop(i)
                count += 1
            if count > 1:
                chars = chars[:i] + list(str(count)) + chars[i:]
                i += len(str(count))
            i += 1
        return len(chars)

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i

    def maxScore(self, s: str) -> int:
        maxi = zeros = 0
        ones = s.count('1')
        for i in range(len(s) - 1):
            ones -= int(s[i] == '1')
            zeros += int(s[i] == '0')
            maxi = max(maxi, zeros + ones)
        return maxi

    def findMatrix2(self, nums: List[int]) -> List[List[int]]:
        res = [set()]
        for num in nums:
            i = 0
            while i < len(res) and num in res[i]: i += 1
            if i < len(res):
                res[i].add(num)
            else:
                res.append(set([num]))
        for i in range(len(res)):
            res[i] = list(res[i])
        return res

    def findMatrix(self, nums: List[int]) -> List[List[int]]:

        counter = [-1] * (len(nums) + 1)
        res = []
        for num in nums:
            counter[num] += 1
            if counter[num] == len(res):
                res.append([])
            res[counter[num]].append(num)

        return res

    def buyChoco(self, prices: List[int], money: int) -> int:
        min1, min2 = float('inf'), float('inf')
        for price in prices:
            if price < min1:
                min1 = price
                if min1 < min2:
                    min1, min2 = min2, min1
        return money if min1 + min2 > money else money - (min1 + min2)

    def maxFrequency(self, nums: List[int], k: int) -> int:
        window = deque()
        pre = 0
        ans = []
        for cur in sorted(nums):
            k -= (cur - pre) * len(window)
            while k < 0:
                k += cur - window.popleft()
            window.append(cur)
            ans.append(len(window))
            pre = cur
        return max(ans)

    def numberOfBeams(self, bank: List[str]) -> int:
        prev = count = 0
        for row in bank:
            if temp := row.count('1'):
                count += temp * prev
                prev = temp
        return count

    def minOperations2(self, nums: List[int]) -> int:
        counter = Counter(nums)
        count = 0
        for val in counter.values():
            if val == 1:
                return -1
            count += val // 3
            if val % 3 != 0:
                count += 1

        return count
        # elif val % 3 == 1:
        #     temp = val
        #     temp
        #
        # elif val % 3 == 2:
        #     count += val // 3 + 1

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def minLength(self, s: str) -> int:
        stack = []
        index = 0
        while index < len(s):
            if not stack:
                stack.append(s[index])
            elif (stack[-1] == 'A' and s[index] == 'B') or (stack[-1] == 'C' and s[index] == 'D'):
                stack.pop()
            else:
                stack.append(s[index])
            index += 1
        return len(stack)

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lose_count = defaultdict(int)
        all_game = set()
        for win, lose in matches:
            lose_count[lose] += 1
            all_game.add(win)
            all_game.add(lose)
        answer0 = [win for win in all_game if win not in lose_count.keys()]
        answer1 = [key for key, val in lose_count.items() if val == 1]
        answer0.sort()
        answer1.sort()
        return [answer0, answer1]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1) + 1, len(text2) + 1
        mat = [['' for _ in range(m)] for __ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                if text1[i - 1] == text2[j - 1]:
                    mat[i][j] = f'{mat[i - 1][j - 1]}{text2[j - 1]}'
                else:
                    mat[i][j] = max([mat[i - 1][j], mat[i][j - 1]], key=len)
        return len(mat[-1][-1])

    def removeDuplicateLetters(self, s: str) -> str:
        st = []
        for i in range(len(s)):
            if s[i] not in st:
                j = len(st) - 1
                while j >= 0 and st[j] > s[i] and st[j] in s[i + 1:]:
                    st.pop()
                    j -= 1
                st.append(s[i])
        return ''.join(st)

    def findTheDifference(self, s: str, t: str) -> str:
        s_c, t_c = [0] * 26, [0] * 26
        for c in s:
            s_c[ord(c) - ord('a')] += 1
        for c in t:
            t_c[ord(c) - ord('a')] += 1
        for i in range(26):
            if s_c[i] < t_c[i]:
                return chr(ord('a') + i)

    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        left, right = 0, len(nums) - 1
        while left < right:
            ans = max(ans, nums[left] + nums[right])
            left += 1
            right -= 1
        return ans

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev, cur = cost[0], cost[1]
        for co in cost[2:]:
            temp = min(cur, prev) + co
            prev = cur
            cur = temp
        return min(cur, prev)

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []
        for i, temp in enumerate(temperatures):
            while st and temperatures[st[-1]] < temp:
                index = st.pop()
                res[index] = i - index
            st.append(i)
        return res


# print(Solution().findWinners(matches=[[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# print(Solution().minLength("ABFCACDB"))
# print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
# print(Solution().minCostClimbingStairs([10,15,20]))

# print(Solution().longestCommonSubsequence(text1="abcde", text2="ace"))
# print(Solution().findTheDifference(s="bcab", t="bcabe"))
# print(Solution().findTheDifference(s="bcabc"))

# print(Solution().numberOfBeams(["011001", "000000", "010100", "001000"]))
# print(Solution().maxFrequency([1, 2, 4], 5))

# print(Solution().minCost(colors="aabaa", neededTime=[1, 2, 3, 4, 1]))
# print(Solution().numRollsToTarget(n=1, k=6, target=3))
# print(Solution().numRollsToTarget(n=2, k=6, target=7))
# print(Solution().compress(["a", "a", "b", "b", "c", "c", "c"]))
# print(Solution().makeEqual(["abc", "aabc", "bc"]))
# print(Solution().maxLengthBetweenEqualCharacters(s="mgntdygtxrvxjnwksqhxuxtrv"))
# print(Solution().numDecodings("11106"))
# print(Solution().onesMinusZeros([[0, 1, 1], [1, 0, 1], [0, 0, 1]]))
# print(Solution().isPathCrossing("NES"))
# print(Solution().isPathCrossing("NESWW"))
# print(Solution().minOperations("10"))
# print(Solution().minOperations2([2, 3, 3, 2, 2, 4, 2, 3, 4]))
# print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
# print(Solution().minOperations("1111"))
# print(Solution().findMatrix([1, 3, 4, 1, 2, 3, 1]))
