class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        set_of_nodes = set()
        for word in words:
            for ch in word:
                set_of_nodes.add(ch)

        for cur_idx in range(1, len(words)):
            word1 = words[cur_idx - 1]
            word2 = words[cur_idx]
            i, j = 0, 0
            while i < len(word1) and j < len(word2) and word1[i] == word2[j]:
                i += 1
                j += 1
            if j == len(word2) and i < len(word1):
                return ""
            if i == len(word1):
                continue
            ch1, ch2 = word1[i], word2[j]
            if ch1 not in adj:
                adj[ch1] = set()
            adj[ch1].add(ch2)

        visiting = set()  # currently in DFS stack (cycle detection)
        visited   = set()  # fully processed
        result    = []

        def dfs(node, path_set) -> bool:
            if node in visited:
                return True
            if node in path_set:      # cycle
                return False
            path_set.add(node)        # mutate the shared set
            for n in adj.get(node, []):
                if not dfs(n, path_set):
                    return False
            path_set.discard(node)    # backtrack
            visited.add(node)
            result.append(node)
            return True

        for node in set_of_nodes:
            if node not in visited:
                if not dfs(node,set()):
                    return ""      # cycle detected

        return "".join(reversed(result))