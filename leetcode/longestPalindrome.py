class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s

        def find_pal(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        ans = ''
        for i in range(n - 1):
            odd = find_pal(i, i)
            even = find_pal(i, i + 1)
            ans = max([odd, even, ans], key=len)
        return ans


print(Solution().longestPalindrome("babad"))
