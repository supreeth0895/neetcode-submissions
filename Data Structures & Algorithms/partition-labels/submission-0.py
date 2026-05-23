class Solution:
    def partitionLabels(self, s: str) -> List[int]:


        #Merge overlapping intervals:
        # "xyxxyzbzbbisl"
        # [[0,3] [1,4] [5,7][6,9] [10,10] [11,11] [12,12]]

        my_map = {}

        for idx,ch in enumerate(s):
            if ch in my_map:
                my_map[ch].append(idx)
            else:
                my_map[ch] = [idx]
        #Get intervsal arr rrady
        my_arr = []
        for ch in s:
            if ch in my_map:
                temp_list = my_map[ch]
                my_arr.append([temp_list[0] , temp_list[len(temp_list)-1]])
                my_map.pop(ch)
        
        print(my_arr)
        #MErge interval:
        ans = []
        cur_interval = my_arr[0].copy()
        end_idx = 1
        while end_idx < len(my_arr):
            print(my_arr[end_idx][0])
            if cur_interval[1] > my_arr[end_idx][0]:
                # print(cur_interval,my_arr[end_idx])
                cur_interval = [cur_interval[0], max(cur_interval[1],my_arr[end_idx][1])]
                # print(cur_interval)
            else:
                # print(cur_interval)
                ans.append(cur_interval[1]-cur_interval[0]+1)
                cur_interval = my_arr[end_idx]
            end_idx = end_idx +1
            
        ans.append(cur_interval[1]-cur_interval[0]+1)
        
        return ans





        


        
        

            
            



                



        