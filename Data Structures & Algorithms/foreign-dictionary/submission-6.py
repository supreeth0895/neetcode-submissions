class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        #INITIALIZE ADJ with ALL CHARS
        adj = {}
        for word in words:
            for ch in word:
                if ch not in adj:
                    adj[ch] = set()


        #POPULATE ADJ
        for cur_idx in range(1, len(words)):
            prev_idx = cur_idx -1
            word1 = words[prev_idx]
            word2 = words[cur_idx]

            char_idx1 = 0
            char_idx2 = 0
            while char_idx1 < len(word1) and char_idx2 < len(word2) and word1[char_idx1] == word2[char_idx2]:
                char_idx1 += 1
                char_idx2 += 1
            if char_idx2 == len(word2) and char_idx1 < len(word1):
                return ""
            if char_idx1 == len(word1) or char_idx2 == len(word2):
                continue
            ch1 = word1[char_idx1]
            ch2 = word2[char_idx2]
            adj[ch1].add(ch2)
        
        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]
            visited[node]  = True
            for neighbor in adj[node]:
                ret_val = dfs(neighbor)
                if ret_val:
                    return True
            visited[node] = False
            answer.append(node)
        
        answer = []

        for ch in adj:
            ret_val = dfs(ch)
            if ret_val == True:
                return ""
        answer.reverse()
        return "".join(answer)
