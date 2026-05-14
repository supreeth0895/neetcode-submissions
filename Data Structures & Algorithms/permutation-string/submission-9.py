#SUPREETH
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s2  < len_s1:
            return False

        #You can either use a map or char array here:
        #Note that comparing the maps or array, is at most O(26) 

        #This entire for loop is O(n) if n is length of s1
        my_map = {}
        for i in range(0, len(s1)):
            if s1[i] not in my_map:
                my_map[s1[i]] = 1
            else:
                my_map[s1[i]] = my_map[s1[i]] + 1
                        
        start = 0
        end = len(s1)

        #O(n)
        my_map2 = {}
        for i in range(start, end):
            ch = s2[i]
            if ch not in my_map2:
                my_map2[ch] = 1
            else:
                my_map2[ch] = my_map2[ch]+1
        if my_map == my_map2:
                return True

        #This is O(m) --> Sliding window
        while end < len(s2):
            
            ch = s2[start]
            if my_map2[ch] == 1:
                my_map2.pop(ch)
            else:
                my_map2[ch] = my_map2[ch] - 1
            
            ch = s2[end]
            if ch not in my_map2:
                my_map2[ch] = 1
            else:
                my_map2[ch] = my_map2[ch]+1
            print(my_map2, my_map)
            start = start+1
            end = end+1


            if my_map == my_map2:
                return True
                
        return False


        #TOTAL TC - O(n+m) = O(n)
        #SC - O(26) = O(1)



        ############################################################################################################################
        # This was my First approach -  O(n*m) . Instead of doing this, having a sliding window can do the same in O(n). I have implemented sliding window above
        # answer = False
        # while end <= len(s2):
        #     if answer:
        #         break
        #     my_map2 = my_map.copy()
        #     for i in range(start, end):
        #         ch = s2[i]
        #         if ch not in my_map2:
        #             break
        #         if my_map2[ch] == 0:
        #             break
        #         else:
        #             my_map2[ch] = my_map2[ch]-1
        #         if i == end-1:
        #             answer = True
        #     start = start+1
        #     end = end+1
        ############################################################################################################################