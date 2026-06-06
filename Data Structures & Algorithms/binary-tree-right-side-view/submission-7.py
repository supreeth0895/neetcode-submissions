# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = []
        q.append(root)
        answer = []
        while len(q) != 0 :
            temp = []
            for idx, elem in enumerate(q):
                if elem.left:
                    temp.append(elem.left)
                if elem.right:
                    temp.append(elem.right)
                if idx == len(q)-1:
                    answer.append(elem.val)
            q = temp
        
        return answer



        