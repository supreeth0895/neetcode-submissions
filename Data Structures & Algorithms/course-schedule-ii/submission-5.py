class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(cur_course, visited):
            if cur_course in visiting:
                return True
            if cur_course in memo:
                return False
            
            visiting.add(cur_course)
            next_courses = my_map.get(cur_course, [])
             
            for course in next_courses:
                if dfs(course, visiting):
                    return True
            
            visiting.remove(cur_course)
            memo.add(cur_course)
            path.append(cur_course)
            return False

        memo = set() # Stores fully processed nodes
        visiting = set() # Stores nodes in current recursion stack
        my_map = {}
        # Reverse logic: map b -> a because b must come before a
        for prereq in prerequisites:
            if prereq[1] in my_map:
                my_map[prereq[1]].append(prereq[0])
            else:
                my_map[prereq[1]] = [prereq[0]]
        
        path = []
        for i in range(numCourses):
            if i not in memo:
                if dfs(i, visiting):
                    return []
        
        return path[::-1]