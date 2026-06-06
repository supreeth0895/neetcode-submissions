# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def helper(preorder, inorder):
            if len(preorder) == 0 and len(inorder) == 0:
                return None
            root = TreeNode(preorder[0])
            root_idx_inorder = 0
            for i in range(0, len(inorder)):
                if inorder[i] == preorder[0]:
                    root_idx_inorder = i
                    len_of_left_subtree = i
                    len_of_right_subtree = len(inorder)-1 - i

            left_subtree_pre_order = preorder[1:1+len_of_left_subtree]
            right_subtree_pre_order = preorder[1+len_of_left_subtree:]

            left_subtree_in_order = inorder[:root_idx_inorder]
            right_subtree_in_order = inorder[root_idx_inorder+1:]

            root.left = helper(left_subtree_pre_order, left_subtree_in_order)
            root.right = helper(right_subtree_pre_order, right_subtree_in_order)
        
            return root
        return helper(preorder, inorder)
        