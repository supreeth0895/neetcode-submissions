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
            if found or not q:
                return 0
            neighbors = set()

            for cur_word in q:
                if diff_between_two_words(cur_word, endWord) == 0:
                    found = True
                    return cur_level

                for word in wordList:
                    if word not in visited:
                        diff_char = diff_between_two_words(cur_word, word)
                        if diff_char == 1:
                            neighbors.add(word)
                            visited.add(word)
                

            q = list(neighbors)

            return bfs(cur_level+1)


        if endWord not in wordList:
            return 0
        
        q=[]
        visited = set()
        found = False
        q.append(beginWord)
        visited.add(beginWord)
        return bfs(1)
