# https://www.lintcode.com/problem/binary-tree-inorder-traversal/description

# Given a binary tree, return the inorder traversal of its nodes' values.

"""
Definition of TreeNode:
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution(object):
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
            res = res + self.inorderTraversal(root.right)
        return res