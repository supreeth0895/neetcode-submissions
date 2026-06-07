class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # BUILD ADJACENCY LIST: prereq -> course (prereq must come before course)
        adj = {}
        for i in range(0, numCourses):
            adj[i] = []
        for p in prerequisites:
            adj[p[1]].append(p[0])  # p[1] is prereq, p[0] is the course that depends on it
        
        def dfs(course):
            nonlocal isCycle, answer
            # If we see a node that's in the current path, we have a cycle
            if course in visiting:
                isCycle = True
                return
            # If already fully processed, skip
            if course in visited:
                return

            # Mark as part of current DFS path
            visiting.add(course)

            # Recurse into all courses that depend on this one
            for pre_req in adj[course]:
                dfs(pre_req)
                if isCycle:
                    return

            # Current course fully processed — append in reverse topological order
            # (prereqs get appended before their dependents as we unwind the stack)
            answer.append(course)
            visiting.remove(course)  # No longer in current path
            visited.add(course)      # Mark as fully processed
           
        answer = []
        visited = set()   # Fully processed nodes
        visiting = set()  # Nodes in the current DFS path (cycle detection)
        isCycle = False

        # Try DFS from every unvisited node to handle disconnected components
        for i in range(0, numCourses):
            if i not in visited:
                dfs(i)
                if isCycle:
                    return []
        
        # Reverse because nodes are appended post-order (dependents before prereqs)
        answer.reverse()
        return answer