
def maximalRectangle(A):
    A = [list(row) for row in A]
    rows = len(A)

    cols = len(A[0])
    max_x = [[0] * cols for _ in range(rows)]
    area1 = 0

    for i in range(rows):
        for j in range(cols):
            if A[i][j] == "0":
                if j == 0:
                    max_x[i][j] = 1
                else:
                    max_x[i][j] = max_x[i][j - 1] + 1

                y = 1
                x = cols

                while i - y + 1 >= 0 and A[i - y + 1][j] == "0":
                    x = min(x, max_x[i - y + 1][j])
                    if x * y > area1:
                        print(i, x, j, y)
                        area1 = max(area1, x * y)
                    y += 1
                # if area1 > area2:
                #     area1, area2 = area2, area1

    return area1


# Example usage
matrix = [['0', '1', '0', '0'],
          ['0', '0', '0', '0'],
          ['0', '0', '0', '1'],
          ['1', '0', '1', '1'],
          ['1', '0', '0', '0'],
          ['1', '1', '0', '0']]

all_rectangles = maximalRectangle(matrix)
# all_rectangles = maximalRectangle(['1000',
#                                    '1000'])
# print(all_rectangles)
def solution_demo(A):
    s = set(A)
    small = 1
    while small in s:
        small += 1
    return small


# # print(solution([1, 3, 6, 4, 1, 2]))
# print(solution([1, 2, 3]))
# print(solution([-1, -3]))

#
def solution_str(letters):
    # Implement your solution here
    charsLower = [False] * 26
    # charsUpper = [False] * 26
    ans = set()
    blackList = set()
    for letter in letters:
        if letter.islower():
            if letter in ans:
                ans.remove(letter)
                blackList.add(letter.upper())
            else:
                charsLower[ord(letter) - 97] = True
        else:
            if  charsLower[ord(letter) - 65] and letter not in blackList:
                ans.add(letter.lower())
            else:
                blackList.add(letter)

    return len(ans)


print(solution_str("aaAbcCABBc"))
print(solution_str("xyzXYZabcABC"))
print(solution_str("ABCabcAefG"))

