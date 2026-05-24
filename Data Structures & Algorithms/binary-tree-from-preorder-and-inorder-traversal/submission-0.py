# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        
        my_map_of_idx = {}
        for i in range(0, len(inorder)):
            my_map_of_idx[inorder[i]] = i
        
        root_val = preorder[0]
        inorder_pivot_idx = my_map_of_idx[root_val]
        len_of_left_subtree = inorder_pivot_idx
        root_node  = TreeNode(root_val)

        root_node.left = self.buildTree(preorder[1:inorder_pivot_idx+1], inorder[:inorder_pivot_idx])
        root_node.right = self.buildTree(preorder[inorder_pivot_idx+1:], inorder[inorder_pivot_idx+1:])
        return root_node