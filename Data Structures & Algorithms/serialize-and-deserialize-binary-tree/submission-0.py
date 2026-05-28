# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ret_str = ""
        q = deque([root])
        while len(q) != 0 :
            elem = q.popleft()
            if elem == None:
                ret_str = ret_str + ",N"
            else:
                ret_str = ret_str + "," + str(elem.val)
                q.append(elem.left)
                q.append(elem.right)
                
        print(ret_str)
        return ret_str[1:]

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        cur_idx = 0
        data_split = data.split(",")
        if data_split[cur_idx] == "N":
            return None

        root = TreeNode(data_split[cur_idx])
        q = deque([root])
        cur_idx = cur_idx+1

        while q:
            node = q.popleft()

            if data_split[cur_idx] == "N":          
                node.left = None
            else:
                node.left = TreeNode(int(data_split[cur_idx]))
                q.append(node.left)
            cur_idx = cur_idx+1

            if data_split[cur_idx] == "N":          
                node.right = None
            else:
                node.right = TreeNode(int(data_split[cur_idx]))
                q.append(node.right)
            cur_idx = cur_idx+1
        return root

