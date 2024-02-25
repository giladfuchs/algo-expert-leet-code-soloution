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

    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        for i in range(26):
            c = chr(ord('a') + i)
            if c in s:
                left = s.index(c)
                right = s.rindex(c)
                if left != right:
                    diff = set()
                    for index in range(left + 1, right):
                        diff.add(s[index])
                    ans += len(diff)
        return ans

    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        size = len(nums)
        if size % 3 != 0:
            return []
        nums.sort()
        ans = []
        for i in range(0, size, 3):
            if i + 2 < size and nums[i + 2] - nums[i] <= k:
                ans.append([nums[i], nums[i + 1], nums[i + 2]])
            else:
                return []
        return ans

    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        for w in words:
            good = True
            for c in w:
                if chars.count(c) < w.count(c):
                    good = False
                    break
            if good:
                count += len(w)
        return count

    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        res = 0
        prev_height = [0] * cols
        for r in range(rows):
            height = matrix[r].copy()
            for c in range(cols):
                if height[c] > 0:
                    height[c] += prev_height[c]

            sorted_height = sorted(height, reverse=True)
            for i in range(cols):
                res = max(res, (i + 1) * sorted_height[i])
            prev_height = height

        return res

    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1 = [0] * 26
        counter2 = [0] * 26
        if len(word1) != len(word2):
            return False
        for c in word1:
            counter1[ord(c) - ord('a')] += 1
        for c in word2:
            counter2[ord(c) - ord('a')] += 1

        for i in range(26):
            if (counter1[i] == 0 and counter2[i] != 0) or \
                    (counter1[i] != 0 and counter2[i] == 0):
                return False
        return sorted(counter1) == sorted(counter2)

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

    def backspaceCompare(self, s: str, t: str) -> bool:
        def create(st):
            ans = []
            for ch in st:
                if ch == '#':
                    ans.pop()
                else:
                    ans.append(ch)
            return ''.join(ans)

        return create(s) == create(t)

    def frequencySort(self, s: str) -> str:
        counter = [0] * 256

        for c in s:
            counter[ord(c)] += 1
        ans = ""
        sumi = sum(counter)
        while sumi > 0:
            index_max = max(range(len(counter)), key=counter.__getitem__)
            ans += chr(index_max) * counter[index_max]
            sumi -= counter[index_max]
            counter[index_max] = 0
        return ans

    def countNicePairs(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        ans = 0
        count = defaultdict(int)
        for num in nums:
            num -= int(str(num)[::-1])
            ans += count[num]
            count[num] += 1
        return ans % mod

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        path = "123456789"
        start, end = len(str(low)), len(str(high))
        res = []
        for i in range(end - start + 1):
            for j in range(len(path) + 1 - (start + i)):
                temp = int(path[j:start + i + j])
                if low <= temp <= high:
                    res.append(temp)
        return res

    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg, res = [], [], []
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        i_p, i_n = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = pos[i_p]
                i_p += 1
            else:
                nums[i] = neg[i_n]
                i_n += 1
        return nums

    def totalMoney(self, n: int) -> int:
        start = 1
        res = 0
        for i in range(0, n, 7):
            res += sum(range(start, min(start + 7, n - i + start)))
            start += 1
        return res

    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] and num[i + 1] == num[i + 2]:
                if not ans or int(ans) < int(num[i:i + 3]):
                    ans = num[i:i + 3]

        return ans

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        d = {word: 1 for word in words}
        for word in words:
            ls_word = list(word)
            for i in range(len(ls_word)):
                temp = ls_word[:]
                temp.pop(i)
                temp_word = ''.join(temp)
                if temp_word in d:
                    d[word] = max(d[temp_word] + 1, d[word])
        return max(d.values())

    def strStr(self, haystack: str, needle: str) -> int:
        try:
            i = haystack.index(needle)
        except:
            i = -1
        return i

    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        words = s.split()
        for i in range(len(words)):
            if pattern[i] in d:
                if d[pattern[i]] != words[i]:
                    return False
            else:
                d[pattern[i]] = words[i]
        return True

    def plusOne(self, digits: List[int]) -> List[int]:
        end = len(digits) - 1
        while end >= 0:

            digits[end] += 1
            if digits[end] != 10:
                break
            else:
                digits[end] = 0
                if end == 0:
                    digits.insert(0, 1)
                end -= 1

        return digits

    def minPartitions(self, n: str) -> int:
        return int(max(list(n)))

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        ans = []
        for i, g in enumerate(groupSizes):
            d[g].append(i)
            if len(d[g]) == g:
                ans.append(d[g][:])
                d[g] = []
        return ans

    def isStrictlyPalindromic(self, n: int) -> bool:

        def to_base(num, base):
            if num == 0:
                return '0'
            digits = []
            while num:
                digits.append(str(num % base))
                num //= base
            return ''.join(digits[::-1])

        for i in range(2, n - 1):
            temp = to_base(n, i)
            if temp != temp[::-1]:
                return False
        return True

    def sortVowels(self, s: str) -> str:
        index = []
        vowels = []
        types = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in range(len(s)):
            if s[i] in types:
                vowels.append(s[i])
                index.append(i)

        vowels.sort()
        st = list(s)
        for i in range(len(index)):
            st[index[i]] = vowels[i]
        return ''.join(st)

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i - 1 < 0:
                        count += 1
                    elif grid[i - 1][j] == 0:
                        count += 1

                    if i + 1 >= len(grid):
                        count += 1
                    elif grid[i + 1][j] == 0:
                        count += 1

                    if j - 1 < 0:
                        count += 1
                    elif grid[i][j - 1] == 0:
                        count += 1

                    if j + 1 >= len(grid[0]):
                        count += 1
                    elif grid[i][j + 1] == 0:
                        count += 1
        return count

# print(Solution().plusOne([9,9,9]))
print(Solution().islandPerimeter([[1,1]]))
# print(Solution().sortVowels("lEetcOde"))
# print(Solution().groupThePeople([3, 3, 3, 3, 3, 1, 3]))
# print(Solution().findWinners(matches=[[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
# print(Solution().sequentialDigits(low=1000, high=13000))
# print(Solution().strStr(haystack="sadbutsad", needle="sad"))
# print(Solution().wordPattern(pattern="abba", s="dog dog dog dog"))
# print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# print(Solution().rearrangeArray([19, -26, -37, -10, -9, 15, 14, 31]))
# print(Solution().divideArray(nums=[1, 3, 4, 8, 7, 9, 3, 5, 1], k=2))
# print(Solution().longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))
# print(Solution().longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))
# print(Solution().largestGoodInteger("6777133338889"))
# print(Solution().totalMoney(20))
# print(Solution().countPalindromicSubsequence("bbcbaba"))
# print(Solution().minLength("ABFCACDB"))
# print(Solution().frequencySort("cccaaa"))
# print(Solution().backspaceCompare("ab##", 'c#d#'))
# print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
# print(Solution().minCostClimbingStairs([10,15,20]))
# print(Solution().countNicePairs([13, 10, 35, 24, 76]))
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
