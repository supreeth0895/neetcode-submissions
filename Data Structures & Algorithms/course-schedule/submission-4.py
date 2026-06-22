class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for src, dest in prerequisites:
            adj[src].append(dest)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if adj[course] == []:
                return True

            visited.add(course)
            for dep in adj[course]:
                if not dfs(dep):
                    return False
            visited.remove(course)
            adj[course] = []
            return True

        res = 0
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
                