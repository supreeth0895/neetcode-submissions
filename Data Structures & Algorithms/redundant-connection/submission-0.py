class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        graph = {}

        def dfs(node, target, visited):
            if node == target:
                return True

            visited.add(node)

            for n_node in graph.get(node, set()):
                if n_node not in visited:
                    if dfs(n_node, target, visited):
                        return True

            return False

        for u, v in edges:

            visited = set()

            # check cycle before adding edge
            if u in graph and v in graph and dfs(u, v, visited):
                return [u, v]

            if u in graph:
                graph[u].add(v)
            else:
                graph[u] = set([v])

            if v in graph:
                graph[v].add(u)
            else:
                graph[v] = set([u])