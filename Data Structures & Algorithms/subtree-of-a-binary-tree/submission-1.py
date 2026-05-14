# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            if subRoot != None:
                return False
        if self.isSame(root,subRoot):
            return True
        else:
            is_subroot_in_left_subtree = self.isSubtree(root.left, subRoot)
            is_subroot_in_right_subtree = self.isSubtree(root.right, subRoot)
            return is_subroot_in_left_subtree or is_subroot_in_right_subtree
    
    def isSame(self, root, subroot):
        if root == None:
            if subroot != None:
                return False
            return True
        
        if subroot == None:
            if root != None:
                return False
            return True
        
        if root.val != subroot.val:
            return False
        is_left_subtree_Same = self.isSame(root.left, subroot.left)
        is_right_subtree_Same = self.isSame(root.right, subroot.right)
        return is_left_subtree_Same and is_right_subtree_Same

        

        

        

        