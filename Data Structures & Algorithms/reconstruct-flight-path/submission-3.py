from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        answer = []
        found_path = False

        my_map = {}
        edge_count = {}
        
        for src, dst in tickets:
            if src not in my_map:
                my_map[src] = []
            my_map[src].append(dst)
            
            if (src, dst) not in edge_count:
                edge_count[(src, dst)] = 0
            edge_count[(src, dst)] += 1

        for key in my_map:
            my_map[key].sort()

        def dfs(cur_node, nodes_travelled):
            nonlocal found_path, answer
            if len(nodes_travelled) == len(tickets) + 1:
                answer = nodes_travelled[:]
                found_path = True
                return True

            if found_path:
                return True

            if cur_node in my_map:
                for neighbor in my_map[cur_node]:
                    if edge_count.get((cur_node, neighbor), 0) > 0:
                        nodes_travelled.append(neighbor)
                        edge_count[(cur_node, neighbor)] -= 1

                        dfs(neighbor, nodes_travelled)
                        if found_path:
                            return True

                        nodes_travelled.pop()
                        edge_count[(cur_node, neighbor)] += 1

            return False

        dfs("JFK", ["JFK"])
        return answer