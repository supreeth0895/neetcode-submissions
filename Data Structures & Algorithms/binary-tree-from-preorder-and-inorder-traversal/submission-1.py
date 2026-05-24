#SUPREETH
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# APPROACH: Divide and Conquer (Recursive)
# -----------------------------------------
# - preorder[0] is always the current root.
# - Find root in inorder → left side = left subtree, right side = right subtree.
# - Recurse on both halves.

# Time: O(N) | Space: O(N)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None

        # Build a value->index map to avoid O(N) search on every call
        my_map_of_idx = {}
        for i in range(len(inorder)):
            my_map_of_idx[inorder[i]] = i

        root_val = preorder[0]
        inorder_pivot_idx = my_map_of_idx[root_val]
        root_node = TreeNode(root_val)

        # Left subtree:  preorder[1..pivot+1], inorder[..pivot]
        root_node.left = self.buildTree(preorder[1:inorder_pivot_idx+1], inorder[:inorder_pivot_idx])

        # Right subtree: preorder[pivot+1..],  inorder[pivot+1..]
        root_node.right = self.buildTree(preorder[inorder_pivot_idx+1:], inorder[inorder_pivot_idx+1:])

        return root_node