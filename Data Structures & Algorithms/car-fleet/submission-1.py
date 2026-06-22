class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tuple_list = []
        for i in range(len(speed)):
            tuple_list.append((position[i], speed[i]))
        tuple_list = sorted(tuple_list, reverse=True)
        fleet = []
        final_time = None
        for pos, pace in tuple_list:
            if not final_time:
                final_time = (target-pos)/pace
                fleet.append((pos, pace, final_time))
            else:
                fleet.append((pos, pace, (target-pos)/pace))
                if fleet[-1][2] <= fleet[-2][2]:
                    fleet.pop()
        return len(fleet)



        