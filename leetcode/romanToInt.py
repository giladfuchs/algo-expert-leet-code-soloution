roman_value = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000, }


class Solution:
    def romanToInt(self, s: str) -> int:
        calc = roman_value[s[-1]]
        i = 0
        while i < len(s) - 1:
            if roman_value[s[i]] < roman_value[s[i + 1]]:
                calc -= roman_value[s[i]]
            else:
                calc += roman_value[s[i]]

            i += 1
        return calc

    def intToRoman(self, num: int) -> str:
        roman_str = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        print({i: j for j, i in roman_value.items()})

    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        mat = [[] for _ in range(numRows)]
        down = True
        x, y = -1, 0
        for c in s:
            if down:
                x += 1
            else:
                x -= 1
                y += 1

            if x == numRows - 1:
                down = False
            size = y - len(mat[x])
            mat[x] += [''] * size + [c]
            if not down and x == 1:
                x = -1
                down = True
        ans = ''
        for row in mat:
            ans += ''.join(row)
        return ans


print(Solution().convert("PAYPALISHIRING", 3))

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 90
# print(Solution().intToRoman("LVIII"))
