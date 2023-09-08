import functools
import pprint


def solution1(commands):
    d = functools.reduce(lambda x, y: {**x, y: x.get(y, 0) + 1}, commands, {_:0 for _ in ['D', 'U']})
    if d["D"] <d['U']:
        return "U"
    if d["D"] > d['U']:
        return "D"
    return ""
def solution3(elements):
    n = len(elements)
    def check(elements):
        for i in range(n-1):
            if elements[i] != n-i:
                return False
        return True
    if check(elements):
        return 0
    for i in range(1, n-1):
        temp_elements = elements[i:] + elements[:i]
        if check(temp_elements):
            return n - i

    return -1
# print(solution3([1, 4, 2, 3]))
# print(solution3([3, 2, 1, 5, 4]))
# print(solution3([2, 1, 8, 7, 6, 5, 4, 3]))
# print(solution3([7, 6, 5, 4, 3, 2, 1, 10, 9, 8]))
#
def solution2(matrix):
    count_remove_all = 0
    index = 0
    count_remove = 0
    ans = []
    rez = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for l in rez:
        a = [i for i, d in enumerate(l)  if d == 'F']
        ans.append(a)
    for i, row in enumerate(matrix):
        if count_remove == 0 and len(set(row)) ==1 and row[0] =='.':
            count_remove +=1

        elif '#'  in row:
            ans.append(row)

            if count_remove:
                ans.append([".", ".", "."])

                count_remove -=1

        else:
            ans.append(row)
    ans = [[".", ".", "."]]*count_remove + ans

    return ans
    # for i, row in enumerate(ans):
    #     if '#' not in row:
    #         count_remove_all +=1



pprint.pprint(solution2(matrix = [
          ["F", "F", "F"],
          [".", "F", "."],
          [".", "F", "F"],
          ["#", "F", "."],
          ["F", "F", "."],
          [".", ".", "."],
          [".", ".", "#"],
          [".", ".", "."]]))




zero = '0'
one = '1'

def solution(binaryString, requests):
    answers = []
    for req in requests:
        if req == 'count':
            answers.append(binaryString.count(one))
        elif req=='flip':
            index = next((i for i, c in enumerate(binaryString) if c==zero),-1)
            binaryString = list(binaryString)
            for i in range(index+1):
                binaryString[i] = zero if binaryString[i] ==one else one
            binaryString = ''.join(binaryString)

            answers.append(index)
    return answers

# print(solution('101000',["count", "flip", "flip", "flip", "count"]))








