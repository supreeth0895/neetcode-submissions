# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            nonlocal max_result
            if not root:
                return 0
            left_subtree_max_path_sum_without_split = helper(root.left)
            right_subtree_max_path_sum_without_split = helper(root.right)

            if left_subtree_max_path_sum_without_split + right_subtree_max_path_sum_without_split + root.val > max_result:
                max_result  = left_subtree_max_path_sum_without_split + right_subtree_max_path_sum_without_split + root.val
            
            #Return max sum without split. If sum is negetive, you just return 0
            return max(0, root.val+left_subtree_max_path_sum_without_split, root.val+right_subtree_max_path_sum_without_split)
        
        max_result = -1000
        left_max = helper(root.left)
        right_max = helper(root.right)
        max_result = max(max_result, left_max+right_max+root.val)
        return max_result
