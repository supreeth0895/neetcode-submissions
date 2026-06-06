#SUPREETH 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(root,subRoot):
            if (root and not subRoot) or (subRoot and not root):
                return False
            # NOTE: We can optimize this further by calling
            # option 3 only if root.val and subroot.val are equal.

            option1 = helper(root.left, subRoot)
            option2 = helper(root.right, subRoot)
            option3 = isSametree(root,subRoot) 
            return option1 or option2 or option3

        def isSametree(p,q):
            if (not p and q) or (not q and p):
                return False
            if (not p) and (not q):
                return True
            if p.val != q.val:
                return False
            is_left_sub_tree_same = isSametree(p.left,q.left)
            is_right_sub_tree_same = isSametree(p.right,q.right)

            if is_left_sub_tree_same and is_right_sub_tree_same:
                return True
            return False


        return helper(root,subRoot)