class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            neighbors = graph.get(node, set()).copy()
            for n_node in neighbors:
                if n_node in graph.get(node, set()):
                    graph[node].remove(n_node)
                    graph[n_node].remove(node)
                dfs(n_node)
                
        graph = {}
        for edge in edges:
            if edge[0] in graph:
                graph[edge[0]].add(edge[1])
            else:
                graph[edge[0]] = set([edge[1]])
            
            if edge[1] in graph:
                graph[edge[1]].add(edge[0])
            else:
                graph[edge[1]] = set([edge[0]])

        number_of_disconnected_graphs = 0
        visited = set()
        for i in range(0,n):
            if i not in visited:
                dfs(i)
                number_of_disconnected_graphs = number_of_disconnected_graphs+1

        return number_of_disconnected_graphs