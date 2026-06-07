class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #BUILD ADJ MATRIX:
        adj = {}
        for i in range(0, numCourses):
            adj[i] = []
        for p in prerequisites:
            adj[p[0]].append(p[1])
        
        #DFS - With Visiting and Visited Tracking. Visiting, is visited elements in the cur path.
        # Once current path is over, you can move to Visited.
        def dfs(course):
            nonlocal isCycle
            if course in visiting:
                isCycle = True
                return
            
            visiting.add(course)
            
            
            for pre_req in adj[course]:
                dfs(pre_req)
            visiting.remove(course)
            


        visited = set()
        isCycle = False
        num_of_nodes_without_pre_req = 0
        for i in range(0, numCourses):
            visiting = set()
            
            dfs(i)
            if isCycle:
                return False
        return True