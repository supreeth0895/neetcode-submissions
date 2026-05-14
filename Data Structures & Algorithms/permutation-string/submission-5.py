class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)
        
        start = 0
        end = len(s1)
        answer = False

        my_map = {}
        for i in range(0, len(s1)):
            if s1[i] not in my_map:
                my_map[s1[i]] = 1
            else:
                my_map[s1[i]] = my_map[s1[i]] + 1


        while end <= len(s2):
            if answer:
                break
            my_map2 = my_map.copy()
            for i in range(start, end):
                ch = s2[i]
                if ch not in my_map2:
                    break
                if my_map2[ch] == 0:
                    break
                else:
                    my_map2[ch] = my_map2[ch]-1
                if i == end-1:
                    answer = True
            start = start+1
            end = end+1
                
        return answer