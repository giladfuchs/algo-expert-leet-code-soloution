class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        start, res = 0, 0
        for i, char in enumerate(s):
            if char in chars and start< chars[char] + 1:
                start = chars[char] + 1

            chars[char] = i
            res = max(res, i - start + 1)

        return res


print(Solution().lengthOfLongestSubstring(s="abba"))
print(Solution().lengthOfLongestSubstring(s="dvdf"))
