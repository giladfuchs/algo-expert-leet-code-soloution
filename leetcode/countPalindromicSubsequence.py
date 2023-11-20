import math


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        chars = [0] * 26
        for i, ch in enumerate(s):
            asc = ord(ch) - 97

            print(asc)


print(Solution().countPalindromicSubsequence("aabca"))
