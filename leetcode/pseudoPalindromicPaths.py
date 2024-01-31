"""
Python program to print all path from root to
leaf in a binary tree
"""
from collections import Counter, defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathsRec(self, root: TreeNode, path: defaultdict):

        if root is None:
            return
        path[root.val] += 1

        if root.left is None and root.right is None:
            if self.can_build_palindrome(path):
                self.paths += 1

        else:
            self.pathsRec(root.left, path, )
            self.pathsRec(root.right, path, )
        path[root.val] -= 1

    def can_build_palindrome(self, count):

        odd_count = 0
        for num in count.values():
            if num % 2 != 0:
                odd_count += 1
                if odd_count > 1:
                    return 0

        return 1

    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        path = defaultdict(int)
        self.paths = 0

        self.pathsRec(root, path)
        return self.paths


#
root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(1)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right.right = TreeNode(1)
print(Solution().pseudoPalindromicPaths(root))
