#SUPREETH2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def helper(preorder_start_idx, pre_order_end_idx, inorder_start_idx, inorder_end_idx):
            if preorder_start_idx > pre_order_end_idx:
                return None
            root = TreeNode(preorder[preorder_start_idx])
            root_idx_inorder = 0
            len_of_left_subtree = 0
            for i in range(inorder_start_idx, inorder_end_idx + 1):
                if inorder[i] == preorder[preorder_start_idx]:
                    root_idx_inorder = i
                    len_of_left_subtree = i - inorder_start_idx
                    break

            root.left = helper(preorder_start_idx + 1, preorder_start_idx + len_of_left_subtree, inorder_start_idx, root_idx_inorder - 1)
            root.right = helper(preorder_start_idx + len_of_left_subtree + 1, pre_order_end_idx,  root_idx_inorder + 1, inorder_end_idx)
        
            return root
        return helper(0, len(preorder)-1, 0, len(inorder)-1)
        