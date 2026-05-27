#TOPOLOGICAL SORT - BASICALLY A POST ORDER DFS
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
                    adj[word1[j]].add(word2[j])
                    break

        result = []
        visited = set()
        path = set()

        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True

            path.add(node)

            for child in adj[node]:
                if not dfs(child):
                    return False

            path.remove(node)
            visited.add(node)
            result.append(node)
            return True

        for node in adj:
            if not dfs(node):
                return ""

        return "".join(reversed(result))