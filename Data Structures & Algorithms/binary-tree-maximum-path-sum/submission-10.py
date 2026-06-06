#SUPREETH2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = -100000
        def helper(root):
            nonlocal max_path

            if not root:
                return 0

            left_subtree_max_path_sum_without_split = max(helper(root.left),0)
            right_subtree_max_path_sum_without_split = max(helper(root.right),0)

            total_subtree_max_path_sum_without_split =  max(left_subtree_max_path_sum_without_split, right_subtree_max_path_sum_without_split,0) + root.val
            total_max_with_split_at_root = left_subtree_max_path_sum_without_split+right_subtree_max_path_sum_without_split+root.val
            max_path = max(max_path, total_max_with_split_at_root)

            return total_subtree_max_path_sum_without_split
        
        helper(root)
        return max_path


            

        