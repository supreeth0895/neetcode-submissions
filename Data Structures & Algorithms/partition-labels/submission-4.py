#SUPREETH
class Solution:
    def partitionLabels(self, s: str) -> List[int]:


        #Merge overlapping intervals:
        # "xyxxyzbzbbisl"
        # [[0,3] [1,4] [5,7][6,9] [10,10] [11,11] [12,12]]

        my_map = {}

        #Has map char-> indices.
        # One optimization is Hashmap need not save all the indices for a character.
        # We can have it save Only last occurance index since we need only that.
        for idx,ch in enumerate(s):
            if ch in my_map:
                my_map[ch].append(idx)
            else:
                my_map[ch] = [idx]
        
        #Get intervals array ready
        my_arr = []
        for ch in s:
            if ch in my_map:
                temp_list = my_map[ch]
                my_arr.append([temp_list[0] , temp_list[len(temp_list)-1]])
                my_map.pop(ch)
        
        
        #Merge interval:
        ans = []
        cur_interval = my_arr[0].copy()
        next_interval_idx = 1
        while next_interval_idx < len(my_arr):
            #If cur_interval and the next_interval (next_idx) can be merged, do it, and update.
            #If not, add cur internval to answer and start new interval

            if cur_interval[1] > my_arr[next_interval_idx][0]:
                cur_interval = [cur_interval[0], max(cur_interval[1],my_arr[next_interval_idx][1])]
            else:
                ans.append(cur_interval[1]-cur_interval[0]+1)
                cur_interval = my_arr[next_interval_idx]
            next_interval_idx = next_interval_idx +1
            
        ans.append(cur_interval[1]-cur_interval[0]+1)
        
        return ans





        


        
        

            
            



                



        