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

    def smallestNumber(self, num: int) -> int:
        str_num = list(str(abs(num)))
        if num > 0:
            str_num.sort()
            if str_num[0] == '0':
                i = 1
                while str_num[i] == '0': i += 1
                str_num[0], str_num[i] = str_num[i], str_num[0]
            return int(''.join(str_num))

        else:
            str_num.sort(reverse=True)
            return -int(''.join(str_num))


# print(Solution().longestPalindrome("babad"))
print(Solution().smallestNumber(310))
print(Solution().smallestNumber(-7605))
