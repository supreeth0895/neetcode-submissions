#SUPREETH2
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def is_diff_in_char_one(word1, word2):           
            counter = 0 
            for i in range(0, len(word1)):
                if word1[i] != word2[i]:
                    counter = counter+1
                    if counter > 1:
                        return False
            
            if counter == 1:
                return True
            return False
        
        q = deque()
        q.append(beginWord)
        visited = set()
        visited.add(beginWord)
        level = 0
        while len(q) != 0 :
            neighbor = []
            while len(q) != 0:
                cur_word = q.popleft()
                if cur_word == endWord:
                    return level+1
                for word in wordList:
                    if word not in visited and is_diff_in_char_one(cur_word, word):
                        neighbor.append(word)
                        visited.add(word)
            print(neighbor)
            level = level +1
            q = deque(neighbor)
        return 0 