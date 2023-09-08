
def isPalindrome(s:str)->bool:
    s = ''.join([_.lower() for _ in s if _.isalnum()])
    return s == s[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))