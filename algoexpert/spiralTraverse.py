from collections import OrderedDict
orderdict = OrderedDict()
orderdict.update({'k': 1})
orderdict.update({'l': 1})
# orderdict.move_to_end('l')
orderdict.popitem()
print()
def spiralTraverse(array):

    n = len(array)
    m = len(array[0])
    ans = []
    visit = [[False for _ in range(m)] for _ in range(n)]

    def up(i,j):
        if not i>0 or visit[i-1][j]:
            right(i,j)
        else:
            i-=1
            visit[i][j] = True
            ans.append(array[i][j])
            up(i,j)
    def left(i,j):
        if not j>0 or visit[i][j-1]:
            if (not i>0 or visit[i-1][j]) and ( i+1 == n or visit[i+1][j]):
                return
            up(i,j)
        else:
            j-=1
            visit[i][j] = True
            ans.append(array[i][j])
            left(i,j)
    def down(i,j):
        if i+1 == n or visit[i+1][j]:
            left(i,j)
        else:
            i+=1
            visit[i][j] = True
            ans.append(array[i][j])
            down(i,j)
    def right(i,j):
        if j+1 == m or visit[i][j+1]:
            down(i,j)
        else:
            j+=1
            visit[i][j] = True
            ans.append(array[i][j])
            right(i,j)

    i, j = 0,0
    visit[i][j] = True
    ans.append(array[i][j])

    right(i,j)
    return ans

print(spiralTraverse([
  [1, 2, 3, 4],
  [12, 13, 14, 5],
  [11, 16, 15, 6],
  [10, 9, 8, 7]
] ))