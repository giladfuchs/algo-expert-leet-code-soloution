

def riverSizes(matrix):
    n = len(matrix)
    m = len(matrix[0])
    visited = [[False for _ in range(m)]
               for _ in range(n)]

    def check(i, j, count):
        visited[i][j] = True

        if i+1<n  and not visited[i+1][j] and  matrix[i+1][j] ==1:
            count = check(i+1,j, count) + 1
        if j+1<m and not visited[i][j+1] and matrix[i][j+1] ==1:
            count = check(i,j+1, count) + 1
        if i-1 >=0  and not visited[i-1][j] and  matrix[i-1][j] ==1:
            count = check(i-1,j, count) + 1
        if j-1 >=0 and not visited[i][j-1] and matrix[i][j-1] ==1:
            count = check(i,j-1, count) + 1

        return count
    ans =  []
    for i, row in enumerate(matrix):
        for j, _ in enumerate(row):
            if not visited[i][j]:
                if _ == 1:
                    temp = check(i, j, 1)
                    ans.append(temp)
                visited[i][j] = True


    return ans

print(riverSizes([
  [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
  [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
  [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
  [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
  [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]
]))