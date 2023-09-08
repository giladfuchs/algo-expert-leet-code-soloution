'''
409. Longest Palindrome
Problem:
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note: Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''


def longest_palindrome_with_list(s: str) -> int:
    arr = [0] * 52
    for char in s:
        if char.lower() == char:
            arr[ord(char) - ord('a')] += 1
        else:
            arr[ord(char) - ord('A')] += 1

    arr = [_ // 2 for _ in arr]
    count = sum(arr) * 2
    return min(count + 1, len(s))

def longest_palindrome_with_set(s: str) -> int:
    hash_set = set()
    res = ''
    get_med_index = lambda x:len(x)//2
    for char in s:
        if char in hash_set:
            hash_set -= set(char)
            med_index_res = get_med_index(res)
            res = ''.join([res[:med_index_res],f'{char}{char}', res[med_index_res:]])
        else:
            hash_set.add(char)

    med_index_res = get_med_index(res)
    temp_res = list(res[:med_index_res])
    temp_res.sort()
    temp_res = ''.join(temp_res)
    res = ''.join([temp_res, temp_res[::-1]])
    if len(hash_set):
        hash_set = list(hash_set)
        hash_set.sort()
        char = hash_set.pop(0)
        med_index_res = get_med_index(res)
        res = ''.join([res[:med_index_res], char, res[med_index_res:]])



    return res


print(longest_palindrome_with_set('lollipop'))
print(longest_palindrome_with_set('aaabb'))
print(longest_palindrome_with_set('aaabbbcc'))
