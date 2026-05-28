#SUPREETH

# Serialize: BFS the tree level by level, recording node values and
# None children as "N", joined by commas.
# Deserialize: Split string by comma, replay BFS — for each node popped
# from queue, assign next two tokens as left and right children.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        ret_str = ""
        q = deque([root])
        while len(q) != 0:
            elem = q.popleft()
            if elem == None:
                # Record null child as "N"
                ret_str = ret_str + ",N"
            else:
                ret_str = ret_str + "," + str(elem.val)
                # Enqueue both children even if None, so nulls are recorded
                q.append(elem.left)
                q.append(elem.right)

        # Strip leading comma
        return ret_str[1:]

    def deserialize(self, data: str) -> Optional[TreeNode]:
        cur_idx = 0
        data_split = data.split(",")

        if data_split[cur_idx] == "N":
            return None

        root = TreeNode(data_split[cur_idx])
        q = deque([root])
        cur_idx = cur_idx + 1

        # For each node in queue, next two tokens are its left and right children
        while q:
            node = q.popleft()

            if data_split[cur_idx] == "N":
                node.left = None
            else:
                node.left = TreeNode(int(data_split[cur_idx]))
                q.append(node.left)
            cur_idx = cur_idx + 1

            if data_split[cur_idx] == "N":
                node.right = None
            else:
                node.right = TreeNode(int(data_split[cur_idx]))
                q.append(node.right)
            cur_idx = cur_idx + 1

        return root