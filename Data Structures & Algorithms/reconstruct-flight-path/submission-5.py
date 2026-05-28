"""
SUPREETH - Reconstruct Itinerary (LeetCode 332)
================================================
Problem:
    Given a list of airline tickets [src, dst], reconstruct the itinerary
    starting from "JFK" that uses every ticket exactly once and is
    lexicographically smallest.

Approach: DFS + Backtracking
    1. Build an adjacency list (my_map) from the tickets.
    2. Sort each airport's neighbor list so we always try the
       lexicographically smallest destination first.
    3. Track remaining uses of each ticket in edge_count to correctly
       handle duplicate routes (e.g. two tickets SFO→ATL).
    4. DFS from "JFK": greedily pick the smallest neighbor, decrement
       its edge count, recurse, and backtrack if a dead end is reached.
    5. The first complete path found (visits len(tickets)+1 nodes) is
       the answer; a found_path flag short-circuits all further work.

Complexity:
    Time  : O(E log E) to sort + O(E!) worst-case backtracking (E = tickets)
    Space : O(E) for the graph and recursion stack

Note: Hierholzer's algorithm solves this in O(E) without backtracking
      and is preferred in interviews for large inputs.
"""

from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        answer = []
        found_path = False  # flag to short-circuit once a valid path is found

        # --- Build graph ---
        my_map = {}      # adjacency list:  airport -> [reachable airports]
        edge_count = {}  # ticket usage tracker: (src, dst) -> remaining uses

        for src, dst in tickets:
            # initialise destination list for this source if needed
            if src not in my_map:
                my_map[src] = []
            my_map[src].append(dst)

            # count available tickets for each (src, dst) pair
            if (src, dst) not in edge_count:
                edge_count[(src, dst)] = 0
            edge_count[(src, dst)] += 1

        # sort neighbors so we always explore lexicographically smaller
        # destinations first — this guarantees the smallest valid itinerary
        for key in my_map:
            my_map[key].sort()

        # --- DFS with backtracking ---
        def dfs(cur_node, nodes_travelled):
            nonlocal found_path, answer

            # base case: all tickets used → valid itinerary found
            if len(nodes_travelled) == len(tickets) + 1:
                answer = nodes_travelled[:]  # copy the current path
                found_path = True
                return True

            # early exit if a solution was already found in another branch
            if found_path:
                return True

            # try each neighbor in sorted (lexicographic) order
            if cur_node in my_map:
                for neighbor in my_map[cur_node]:
                    # only use this edge if tickets remain for it
                    if edge_count.get((cur_node, neighbor), 0) > 0:
                        nodes_travelled.append(neighbor)
                        edge_count[(cur_node, neighbor)] -= 1  # use ticket

                        dfs(neighbor, nodes_travelled)
                        if found_path:
                            return True  # propagate success immediately

                        # backtrack: restore state and try the next neighbor
                        nodes_travelled.pop()
                        edge_count[(cur_node, neighbor)] += 1  # return ticket

            return False  # no valid path found from this node

        # kick off DFS from the mandatory starting airport
        dfs("JFK", ["JFK"])
        return answer