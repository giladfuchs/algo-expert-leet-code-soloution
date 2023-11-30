from collections import defaultdict


def longestSubstringWithoutDuplication(string):
    d = defaultdict(lambda: -1)
    longest = ''
    pos = 0
    for i, char in enumerate(string):
        pos = max(pos, d[char] + 1)
        if i + 1 - pos > len(longest):
            longest = string[pos:i + 1]

        d[char] = i
    return longest


print(longestSubstringWithoutDuplication("abacacacaaabacaaaeaaafa"))  # bac
# print(longestSubstringWithoutDuplication("clementisacap"))  # mentisac
# print(longestSubstringWithoutDuplication("a"))  # mentisac
