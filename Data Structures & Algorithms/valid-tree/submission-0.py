class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        adj = defaultdict(list)
        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)
        
        visited = set()
        def dfs(root, prev):
            if root in visited:
                return False
            visited.add(root)
            for neigh in adj[root]:
                if neigh == prev:
                    continue
                val = dfs(neigh, root)
                if not val:
                    return False
            return True
        return dfs(0, -1) and len(visited) == n
