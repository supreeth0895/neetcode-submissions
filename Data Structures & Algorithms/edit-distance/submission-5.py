class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def backtrack(cur_idx1, cur_idx2):
            if (cur_idx1,cur_idx2) in memo:
                return memo[(cur_idx1,cur_idx2)]
            if cur_idx2 == len(word2):
                return 1*(len(word1) - cur_idx1)
            if cur_idx1 == len(word1):
                return 1*(len(word2) - cur_idx2)

            ch1 = word1[cur_idx1]
            ch2 = word2[cur_idx2]
            if  ch1 == ch2:
                option1 = backtrack(cur_idx1+1, cur_idx2+1)
                memo[(cur_idx1,cur_idx2)] = option1
                return option1
            option1 = 1+backtrack(cur_idx1, cur_idx2+1) #add a letter  in word1
            option2 = 1+backtrack(cur_idx1+1, cur_idx2) #delete a letter  in word1
            option3 = 1+backtrack(cur_idx1+1, cur_idx2+1) #replace the letter  in word1

            memo[(cur_idx1,cur_idx2)] = min(option1,option2,option3)
            return min(option1,option2,option3)
        
        memo = {}
        return backtrack(0,0)