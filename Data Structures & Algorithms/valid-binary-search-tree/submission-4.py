# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, -1001, 1001)
    
    def helper(self, root, left_bound, right_bound):
        if not root:
            return True
        if root.val >= right_bound or root.val <= left_bound:
            return False
        is_left_subtree_valid_BST, is_right_subtree_valid_BST = True, True
        if root.left:
            new_right_bound = min(right_bound,root.val)
            is_left_subtree_valid_BST = self.helper(root.left,left_bound, new_right_bound)
        if root.right:
            new_left_bound = max(left_bound,root.val)
            is_right_subtree_valid_BST = self.helper(root.right,new_left_bound, right_bound)
        
        return is_left_subtree_valid_BST and is_right_subtree_valid_BST

#If you know that for BST if we do in order traversal, it will be in ascwending order, we can do that, but that willl have space O(n) instead of O(1)
        
        