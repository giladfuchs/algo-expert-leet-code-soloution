import functools
from typing import List


# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         start_idx = 0
#         for i in range(1, len(s)+1):
#             if s[start_idx:i] in wordDict:
#                 start_idx = i
#         return start_idx==len(s)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        @functools.lru_cache(None)
        def wordBreak(i: int) -> bool:
            """Returns True if s[i:] can be segmented."""
            if i == len(s):
                return True
            return any(s[i:j] in wordSet and wordBreak(j) for j in range(i + 1, len(s) + 1))

        return wordBreak(0)

    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        kMax = 2000

        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        return a if a < kMax else ~(a ^ mask)


if __name__ == '__main__':
    # print(Solution().wordBreak(s="leetcode", wordDict=["leet", "code"]))
    # print(Solution().wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
    # print(Solution().wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
    print(Solution().getSum(a=-2, b=3))
