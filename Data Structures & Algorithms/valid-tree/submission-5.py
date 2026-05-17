class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def dfs(node, visited):
            overall_visited.add(node)
            if node in visited:
                return True
            visited.add(node)

            neighbors = graph.get(node, set()).copy()
            for neighbor in neighbors:
                if neighbor in graph[node]:
                    graph[node].remove(neighbor)
                    graph[neighbor].remove(node)
                    if dfs(neighbor, visited.copy()):
                        return True
            
            return False
        
        graph = {}
        for edge in edges:
            if edge[0] == edge[1]:
                return False
            if edge[0] in graph:
                graph[edge[0]].add(edge[1])
            else:
                graph[edge[0]] = set([edge[1]])
            
            if edge[1] in graph:
                graph[edge[1]].add(edge[0])
            else:
                graph[edge[1]] = set([edge[0]])

        if not edges:
            return n == 1        
        overall_visited = set()
        visited = set()
        is_cyclic = dfs(0, visited)
        if len(overall_visited) != n:
            return False
        if is_cyclic:
            return False
        return True