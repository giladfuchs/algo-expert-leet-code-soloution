# def isPalindrome(string):
#     return string == string[::-1]
class Solution:

    def isPalindrome(self, s: str) -> bool:
        s = [ch.lower() for ch in s if ch.isalpha() or ch.isnumeric()]
        return s == s[::-1]

    def isSubsequence(self, s: str, t: str) -> bool:
        position = 0
        n = len(s)
        for i in range(len(t)):
            if position < n:
                if s[position] == t[i]:
                    position += 1
            else:
                break
        return position == n


print(Solution().isSubsequence(s="abc", t="ahbgdc"))
print(Solution().isSubsequence( s = "axc", t = "ahbgdc"))
# print(Solution().isPalindrome("0P"))
# print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
# print(Solution().isPalindrome("race a car"))
