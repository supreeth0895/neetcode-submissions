# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        result = ""
        q = deque()
        q.append(root)
        while len(q) != 0:
            elem = q.popleft()
            if elem.val == -1001:
                result = result + ",N"
                continue

            if elem.left:
                q.append(elem.left)
            else:
                q.append(TreeNode(-1001))
            if elem.right:
                q.append(elem.right)
            else:
                q.append(TreeNode(-1001))
            
            
            result = result + "," + str(elem.val)
        print(result)
        return result[1:]

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:
            return None
        data_split = data.split(",")

        cur_idx = 0
        q = deque()
        root = TreeNode(int(data_split[0]))
        q.append(root)
        cur_idx = cur_idx+1
        
        while len(q) != 0 :
            temp = q.copy()
            for elem in temp:
                if data_split[cur_idx] != "N":
                    elem.left = TreeNode(int(data_split[cur_idx]))
                    q.append(elem.left)
                else:
                    elem.left = None
                cur_idx = cur_idx+1
                if data_split[cur_idx] != "N":
                    elem.right = TreeNode(int(data_split[cur_idx]))
                    q.append(elem.right)
                else:
                    elem.right = None
                cur_idx = cur_idx+1
                q.popleft()
        return root



                
                    
                

            



