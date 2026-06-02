class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for word in words:
            for ch in word:
                adj[ch] = set()

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""
            for j in range(min_len):
                if word1[j] != word2[j]:
                    adj[word2[j]].add(word1[j])
                    break

        result = []
        visited = set()

        def dfs(node, path):
            if node in path:
                return False
            if node in visited:
                return True


            for child in adj[node]:
                new_path = path.copy()
                new_path.add(node)
                if not dfs(child, new_path):
                    return False
            visited.add(node)
            result.append(node)
            return True
        

        for node in adj:
            if not dfs(node, set()):
                return ""

        return "".join(result)