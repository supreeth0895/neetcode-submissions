from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(cur_course, visited):
            if cur_course in memo:
                return memo[cur_course]

            if cur_course in visited:
                memo[cur_course] = True
                return True  # cycle

            visited.add(cur_course)

            if cur_course in my_map:
                for course in my_map[cur_course]:
                    # IMPORTANT: still copy, as you intended
                    if dfs(course, visited.copy()):
                        memo[cur_course] = True
                        return True

            memo[cur_course] = False

            # only add after fully exploring
            path.append(cur_course)

            return False

        memo = {}
        my_map = {}

        for course, pre in prerequisites:
            my_map.setdefault(pre, []).append(course)

        visited = set()
        path = []

        # run DFS from every node (no fake node)
        for i in range(numCourses):
            if dfs(i, visited.copy()):
                return []

        return path[::-1]