def fourNumberSum(array, targetSum):
    array.sort()

    ans = []
    d = {}
    n = len(array)
    for i in range(n):
        for j in range(i+1,n):
            temp_key = array[i] + array[j]
            if temp_key in d:
                d[temp_key].append([i,j])
            else:
                d[temp_key] = [[i,j]]

    array.sort()
    d_keys = list(d.keys())
    start = 0
    end = len(d_keys)-1
    while start< end:
        temp_sum = d_keys[start] + d_keys[end]
        if temp_sum == targetSum:
            to_add = [[[array[index] for index in i] + [array[index] for index in j]]
                      for i, j in zip(d[d_keys[start]], d[d_keys[end]])
                      if
                      all(x not in j for x in i)]



    for _ in d_keys:
        temp_key = targetSum - _
        if temp_key in d and _ in d:
            to_add = [[[array[index] for index in i]+[array[index] for index in j]]
                      for i, j in zip( d[temp_key],  d[_])
                      if
                      all(x not in j for x in i)]
            if to_add:
                ans.extend(to_add)
                del d[temp_key]
                if _ in d:
                    del d[_]

    return ans

    for _ in d_keys:
        start = 0
        end = n-1

        while start<end:

            temp_key = targetSum - ( array[start] + array[end])
            if temp_key in d:
                to_add = [[array[start] , array[end], array[arr[0]], array[arr[1]]] for arr in d[temp_key] if  all(x not in arr for x in [start, end])]
                if to_add:
                    ans.extend(to_add)
                    del d[temp_key]
                start += 1
                end -= 1
            elif temp_key > 0:
                start += 1
            else:
                end -= 1

    return ans

# print(fourNumberSum([7, 6, 4, -1, 1, 2],16))

def threeNumberSum(array, targetSum):
    ans = []
    def check(i, temp):
        if len(temp)==3:
            if sum(temp) == targetSum:
                ans.append(list(temp))
            return
        if i == len(array):
            return
        temp.append(array[i])
        check(i+1, temp)
        temp.pop()
        check(i+1, temp)

    check(0,[])
    ans = [sorted(_) for _ in ans]
    ans.sort()
    return ans
# Write your code here.
def threeNumberSum2(array, targetSum):
    array.sort()
    ans = []
    i = 0
    len_arr = len(array)-1
    while i<len_arr:
        start = i+1
        end =len_arr
        while start<end:
            temp_arr = [array[i], array[start], array[end]]
            temp_sum = sum(temp_arr)
            if temp_sum == targetSum:
                ans.append(temp_arr)
                start+=1
                end-=1
            elif temp_sum<targetSum:
                start+=1
            else:
                end-=1

        i+=1


    print(ans)
    return ans
# threeNumberSum2([12, 3, 1, 2, -6, 5, -8, 6],0)

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    if tree ==None:
        return True
    if tree.left!=None:
        if not tree.value >= tree.left.value:
            return False
    if tree.right!=None:
        if not tree.value <= tree.right.value:
            return False
    return validateBst(tree.left) and validateBst(tree.right)
root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(12)
root.right.right = BST(22)
print(validateBst(root))