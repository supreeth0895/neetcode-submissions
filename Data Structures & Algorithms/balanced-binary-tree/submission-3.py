# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return 0, True
            left_subtree_height, is_left_subtree_balanced = helper(root.left)
            right_subtree_height, is_right_subtree_balanced = helper(root.right)
            is_balanced = is_left_subtree_balanced and is_right_subtree_balanced
            if abs(left_subtree_height - right_subtree_height) > 1 :
                is_balanced = False
            return max(left_subtree_height, right_subtree_height)+1, is_balanced

        return helper(root)[1]

        