class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)
        
        def dfs(root):
            visited.add(root)
            for neigh in adj[root]:
                if neigh in visited:
                    continue
                dfs(neigh)

        res = 0
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            dfs(i)
            res+=1
        return res