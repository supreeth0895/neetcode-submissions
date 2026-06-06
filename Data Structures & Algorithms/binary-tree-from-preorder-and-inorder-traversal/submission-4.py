#SUPREETH2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#SC - O(1)
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


# I was able to come up with SC- O(n) without any help from AI.
# To improve SC, we need not pass preorder and inorder slices again and again,
# rather we can pass indexes to the array boundrries.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

#         def helper(preorder, inorder):
#             if len(preorder) == 0 and len(inorder) == 0:
#                 return None
#             root = TreeNode(preorder[0])
#             root_idx_inorder = 0
#             for i in range(0, len(inorder)):
#                 if inorder[i] == preorder[0]:
#                     root_idx_inorder = i
#                     len_of_left_subtree = i
#                     len_of_right_subtree = len(inorder)-1 - i

#             left_subtree_pre_order = preorder[1:1+len_of_left_subtree]
#             right_subtree_pre_order = preorder[1+len_of_left_subtree:]

#             left_subtree_in_order = inorder[:root_idx_inorder]
#             right_subtree_in_order = inorder[root_idx_inorder+1:]

#             root.left = helper(left_subtree_pre_order, left_subtree_in_order)
#             root.right = helper(right_subtree_pre_order, right_subtree_in_order)
        
#             return root
#         return helper(preorder, inorder)
        
        