class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_tuple_list = []
        for i in range(0, len(position)):
            sorted_tuple_list.append(tuple([position[i],speed[i]]))
        
        sorted_tuple_list.sort(reverse = True)

        st = []

        for entry in sorted_tuple_list:
            remaining_miles = target - entry[0]
            vehicle_speed = entry[1]
            remaining_time = remaining_miles/vehicle_speed
            if len(st) == 0:
                st.append(remaining_time)
            elif remaining_time <= st[len(st)-1]:
                continue
            else:
                st.append(remaining_time)
        return len(st)
                

#The only reason to use monotonic stack here is cars cannot pass one another.
#that's the reason we sort as well.
#Car at mile #7, will either reach before or at same time as car at mile #5 irrespective of speed
