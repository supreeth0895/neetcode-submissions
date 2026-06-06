# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(p,q):
            if not p and not q:
                return True
            if (not p and q) or (p and not q):
                return False
            if p.val != q.val:
                return False
            is_left_subtree_same  = helper(p.left, q.left)
            is_right_subtree_same = helper(p.right, q.right)
            return is_left_subtree_same and  is_right_subtree_same
        return helper(p,q)
        