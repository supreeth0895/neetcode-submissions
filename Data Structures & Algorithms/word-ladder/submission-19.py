class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def diff_between_two_words(str1, str2):
            cur_len = 0
            for i,ch in enumerate(str1):
                if str1[i] != str2[i]:
                    cur_len = cur_len+1
            return cur_len

        def bfs(cur_level):
            nonlocal q, found
            if len(q) == 0 or found:
                return 0
            neighbors = set()

            for cur_word in q:
                visited.add(cur_word)
                if cur_word == endWord:
                    found = True
                    return cur_level
                for i in range(0,len(cur_word)):
                    new_str = cur_word[:i] + "*" + cur_word[i+1:]
                    # print(cur_word, new_str)
                    if new_str in my_map:
                        for val in my_map[new_str]:
                            if val not in visited:
                                neighbors.add(val)
            print(q)
            q = []        
            q = list(neighbors)
            print(q)
            return bfs(cur_level+1)


        if endWord not in wordList:
            return 0
        my_map = {}
        # 1. Pre-process patterns: O(N * L^2)
        # N = number of words, L = word length
        for w in wordList:
            for i in range(0,len(w)):
                new_str = w[:i] + "*" + w[i+1:]
                if new_str in my_map:
                    my_map[new_str].append(w)
                else:
                    my_map[new_str] = [w]
        

        
        q=[]
        visited = set()
        found = False
        q.append(beginWord)
        visited.add(beginWord)
        return bfs(1)



# BFS approach - But this is not most optimal, because every iteration, we are checking ALL the words.
# Opimal way is to preprossess all patterns and store them in a hashmap before - 
# Example: for hot, we would store *ot h*t, and ho* as the keys pointing to value hot
#when looking for neighbors of string we would look similar way.
# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         def diff_between_two_words(str1, str2):
#             cur_len = 0
#             for i,ch in enumerate(str1):
#                 if str1[i] != str2[i]:
#                     cur_len = cur_len+1
#             return cur_len

#         def bfs(cur_level):
#             nonlocal q, found
#             if found or not q:
#                 return 0
#             neighbors = []

#             for cur_word in q:
#                 if diff_between_two_words(cur_word, endWord) == 0:
#                     found = True
#                     return cur_level

#                 for word in wordList:
#                     if word not in visited:
#                         diff_char = diff_between_two_words(cur_word, word)
#                         if diff_char == 1:
#                             neighbors.append(word)
#                             visited.add(word)
#             q = neighbors
#             return bfs(cur_level+1)


#         if endWord not in wordList:
#             return 0
#         q=[]
#         visited = set()
#         found = False
#         q.append(beginWord)
#         visited.add(beginWord)
#         return bfs(1)