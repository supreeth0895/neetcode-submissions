# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if (p == None and q != None) or (p != None and q == None):
            return False
        if p.val != q.val:
            return False
        else:
            is_left_subtree_same = self.isSameTree(p.left,q.left)
            is_right_subtree_same = self.isSameTree(p.right,q.right)
            return is_left_subtree_same and is_right_subtree_same
