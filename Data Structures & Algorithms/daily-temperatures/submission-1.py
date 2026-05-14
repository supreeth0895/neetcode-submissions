class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        st = [] #pair[temp, index]

        for i,temp in enumerate(temperatures):
            if len(st) == 0:
                st.append([temp,i])
                continue
            while temp > st[len(st)-1][0]:
                val = st.pop()
                temp_index = val[1]
                output[temp_index] = i - temp_index
                if len(st) == 0 :
                    break
            st.append([temp,i])
        
        return output

#Here we have used Increasing Monotonic stack 
        