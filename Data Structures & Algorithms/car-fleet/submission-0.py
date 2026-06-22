class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tuple_list = []
        for i in range(len(speed)):
            tuple_list.append((position[i], speed[i]))
        tuple_list = sorted(tuple_list, reverse=True)
        fleet = []
        for pos, pace in tuple_list:
            fleet.append((target-pos)/pace)
            if len(fleet)>=2 and fleet[-1] <= fleet[-2]:
                fleet.pop()
        return len(fleet)

        