def longestCommonSubsequence(str1, str2):
    str1, str2 = list(str1), list(str2)
    n, m = len(str1) + 1, len(str2) + 1
    matrix = [['' for _ in range(m)] for __ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            if str1[i - 1] == str2[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + str2[j-1]
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1], key=len)
    return list(matrix[-1][-1])

def longestCommonSubsequenceBackTrack(str1, str2):
    str1, str2 = list(str1), list(str2)
    n, m = len(str1) + 1, len(str2) + 1

    matrix = [[{"st":None, "size":0, "i":None, "j":None} for _ in range(m)] for __ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            if str1[i - 1] == str2[j-1]:
                matrix[i][j] ={"st":str1[i - 1], "size":1+matrix[i-1][j-1].get('size'), "i":i-1, "j":j-1}

            elif matrix[i-1][j].get('size') > matrix[i][j-1].get('size'):
                matrix[i][j] ={"st":None, "size":matrix[i-1][j].get('size'), "i":i-1, "j":j}
            else:
                matrix[i][j] ={"st":None, "size":matrix[i][j-1].get('size'), "i":i, "j":j-1}


    n -=1
    m -=1
    ans = []
    while n and m:
        end = matrix[n][m]
        n, m, st = end.get('i'), end.get('j'), end.get('st')
        if st:
            ans.append(st)

    return ans[::-1]

print(longestCommonSubsequence(list("8111111111111111142"), list("222222222822222222222222222222433333333332")))