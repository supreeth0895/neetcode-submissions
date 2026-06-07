class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #BUILD ADJ MATRIX:
        adj = {}
        for i in range(0, numCourses):
            adj[i] = []
        for p in prerequisites:
            adj[p[1]].append(p[0])
        
        #DFS - With Visiting and Visited Tracking. Visiting, is visited elements in the cur path.
        # Once current path is over, you can move to Visited.
        def dfs(course):
            nonlocal isCycle, answer
            if course in visiting:
                isCycle = True
                return
            if course in visited:
                return

            
            visiting.add(course)
            for pre_req in adj[course]:
                dfs(pre_req)
                if isCycle:
                    return
            answer.append(course)
            visiting.remove(course)
            visited.add(course)
           
 
        answer = []
        visited = set()
        visiting = set()
        isCycle = False
        num_of_nodes_without_pre_req = 0
        for i in range(0, numCourses):
            if i not in visited:
                dfs(i)
                if isCycle:
                    return []
        answer.reverse()
        return answer