# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root,min_val,max_val):
            if not root:
                return True
            if root.val <= min_val or root.val >= max_val:
                return False
            is_left_subtree_valid = helper(root.left,min_val, root.val)
            is_right_subtree_valid = helper(root.right, root.val, max_val)
            return is_left_subtree_valid and is_right_subtree_valid
        return helper(root,-100000,100000)


        