#SUPREETH

# This is simple logic. Visualize it like a graph. =
# If there is a proper starting point, and no cycles in the graph, (ie; every node is visited once), we can do it.
#Else return false

# How to denote this as a graph using map:
# My Map {
#     0 : 1,2,3 # Course 0 is the prereq for course 1,2 3
#     1:23 - Course 1 is the prereq for 2,3
#     2: 3 - Course 2 is the prereq for 3
# }
# 3 is not in map- so should be starting point


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(cur_course,visited):
            if cur_course in visited:
                return True
            if cur_course not in my_map:
                return False
            next_courses = my_map[cur_course]
            visited.add(cur_course)
            for course in next_courses:
                new_visited = visited.copy()
                ret_val = dfs(course, new_visited)
                if ret_val:
                    return True
            
            return False

        my_map = {}
        #Our Graph is ready
        for prereq in prerequisites:
            if prereq[1] in my_map:
                my_map[prereq[1]].append(prereq[0])
            else:
                my_map[prereq[1]] = [prereq[0]]
        
        all_pre_reqs = set()
        #Find potential start points, ie; nodes with no pre req:
        for prereq in prerequisites:
            all_pre_reqs.add(prereq[1])
        
        my_map[-1] = list(all_pre_reqs)
        visited = set()
        
        iscyclic = dfs(-1, visited)
        return not iscyclic