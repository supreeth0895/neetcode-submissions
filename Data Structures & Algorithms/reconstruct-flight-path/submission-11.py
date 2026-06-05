class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        tickets.sort(reverse=True)
        answer = []
        print(tickets)

        for i, ticket in enumerate(tickets):
            if ticket[0] in adj:
                adj[ticket[0]].append((ticket[1]))
            else:
                adj[ticket[0]] = [(ticket[1])]

        start_node  = "JFK"

        #Since we know that 1 valid solution exisits, no need to backtrack.
        # for each outging edge, pop it from tickets and DFS into it.
        #When no edges remain, add source to answer
        def dfs(source_node):
            while source_node in adj and adj[source_node]:
                dest_node = adj[source_node].pop()
                #call dfs on destination_node
                dfs(dest_node)
            answer.append(source_node) #This will construct result in reverse order, from the end of itenerary.

        dfs(start_node)
        answer.reverse()
        return answer



# #SUPREETH -2 :  DFS - But some twists:
# # duplicate tickets allowed: consider ticket index in visited
# # other than that, just track the paths, and visited.
# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         adj = {}
#         tickets.sort()
#         # Note: duplicate tickets may exist (e.g. two ["TIA","ANU"] tickets),
#         # so we track visited edges by index also, rather than just (src, dst) tuple
#         # to correctly allow using each ticket independently
#         for i, ticket in enumerate(tickets):
#             if ticket[0] in adj:
#                 adj[ticket[0]].append((ticket[1], i))
#             else:
#                 adj[ticket[0]] = [(ticket[1], i)]
        
#         start_node  = "JFK"

#         answer = []
#         answer_found = False

#         def dfs(cur_node, path, visited_tickets):
#             nonlocal answer, answer_found
#             if answer_found:
#                 return

#             new_path = path[:]
#             new_path.append(cur_node)

#             if len(visited_tickets) == len(tickets):
#                 answer = new_path[:]
#                 answer_found = True
#                 return 
            
#             if cur_node in adj:
#                 for node,i in adj[cur_node]:
#                     if (cur_node, node, i) not in visited_tickets:
#                         visited_tickets_copy = visited_tickets.copy()
#                         visited_tickets_copy.add((cur_node, node, i))
#                         dfs(node,new_path, visited_tickets_copy)
            
            
            

#         dfs(start_node, [], set())
#         return answer

            
        