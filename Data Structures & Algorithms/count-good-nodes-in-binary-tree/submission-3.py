#SUPREETH
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.answer = []

    def goodNodes(self, root: TreeNode) -> int:
        self.helper(root, root.val)
        return len(self.answer)
    
    def helper(self, root, max_val):
        if not root:
            return
        new_max_val = max_val
        if root.val >= max_val:
            self.answer.append(root.val)
            new_max_val = root.val
        self.helper(root.left, new_max_val)
        self.helper(root.right, new_max_val)





        