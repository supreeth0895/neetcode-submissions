#SUPREETH
# SUMMARY:
# DFS through the tree. At each node, compute the best path sum that
# passes through it (left + root + right). Track global max across all nodes.
# Return only the best single-side path (no split) up to the parent.

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

            # Recurse on children; get best path sum going downward (no split)
            left_subtree_max_path_sum_without_split = helper(root.left)
            right_subtree_max_path_sum_without_split = helper(root.right)

            # Check if path through current node (with split) is the global best
            if left_subtree_max_path_sum_without_split + right_subtree_max_path_sum_without_split + root.val > max_result:
                max_result = left_subtree_max_path_sum_without_split + right_subtree_max_path_sum_without_split + root.val
            
            # Return best path going through this node in one direction only.
            # Return 0 if both options are negative (parent is better off ignoring this subtree)
            return max(0, root.val+left_subtree_max_path_sum_without_split, root.val+right_subtree_max_path_sum_without_split)
        
        max_result = -1000
        left_max = helper(root.left)
        right_max = helper(root.right)
        max_result = max(max_result, left_max+right_max+root.val)
        return max_result