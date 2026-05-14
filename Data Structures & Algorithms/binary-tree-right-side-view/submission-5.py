#SUPREETH
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.q = []
        level_orer_list = []
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        self.q.append(tuple([root,0]))
        return self.helper(root)
    
    def helper(self, root):
        children = []
        ptr = 0
        while ptr < len(self.q) :
            val = self.q[ptr]
            node = val[0]
            level = val[1]
            if node.left:
                self.q.append(tuple([node.left, level+1]))
            if node.right:
                self.q.append(tuple([node.right, level+1]))
            ptr = ptr+1
        
        answer = []
        i = 0
        for i in range(0, len(self.q)):
            if i == len(self.q)-1:
                answer.append(self.q[i][0].val) 
                continue
            if  self.q[i+1][1] != self.q[i][1]:
                answer.append(self.q[i][0].val)
            print(self.q[i][0].val,  i)
            
       
                    
        return answer
        #For every children, Get thier children and remove the parent from the queue