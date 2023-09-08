import random
from functools import reduce
from typing import Optional, List
 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTreeHelp(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTreeHelp(root.right)
        self.invertTreeHelp(root.left)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invertTreeHelp(root)
        return root

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = [0]

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], left + right)

            return 1 + max(left, right)

        dfs(root)
        return res[0]

    def condition_height(self, left_height: int or bool, right_height: int or bool) -> int:
        return left_height is not False and right_height is not False and abs(left_height-right_height) <2

    def check_height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_height = self.check_height(root.left)
        right_height = self.check_height(root.right)
        if not self.condition_height(left_height=left_height, right_height=right_height):
            return False
        return max(left_height, right_height) + 1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_height = self.check_height(root.left)
        right_height = self.check_height(root.right)
        return self.condition_height(left_height=left_height, right_height=right_height)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p==None and q!=None )or (p!=None and q==None ) or p.val!= q.val:
            return False
        if p == None:
            return True
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid_bst(node: Optional[TreeNode], left: float, right: float):
            if node is None:
                return True
            if (left >= node.val) or (right <= node.val):
                return False
            return is_valid_bst(node.left, left, node.val) and is_valid_bst(node.right, node.val, right)
        return is_valid_bst(root, float('-inf'), float('inf'))
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        sum = 0
        for s in tokens:
            try:
                temp_num = int(s)
                stack.append(temp_num)
            except:
                second = stack.pop()
                first = stack.pop()

                sum = int(eval(f'{first} {s} {second}'))
                stack.append(sum)
        return int( stack.pop())


import time
import datetime
def a(x,y):
    # print(x,y)
    return { **x, y: x[y]+1 if y in x.keys() else 1 }
result = reduce(a, [1,1,2,3,4,2,1,5,4,5],{})
string = "20/01/2020"
print(result)
b=[]
for i in range(12):
    string = f"20/01/{random.randint(1000,10000)}"
    element = datetime.datetime.strptime(string, "%d/%m/%Y")
    b.append(element)
def comp(x,y):
    return x<y
c = sorted(b,key=comp)
print(b)
#
# a = TreeNode(1, TreeNode(2,TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(6, TreeNode(1), TreeNode(1, TreeNode(1)))))
# print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
# print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
# print(Solution().evalRPN(["4","13","5","/","+"]))
# print(Solution().isBalanced(a))