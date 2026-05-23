class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        gas_left_for_index = [0]* len(gas)
        for i in range(0, len(gas)):
            gas_left_for_index[i] = gas[i]-cost[i]
        cur_total = 0
        start_idx = 0
        for i in range(0, len(gas)):
            if cur_total < 0:
                cur_total = 0
                start_idx = i
            cur_total = cur_total + gas_left_for_index[i]
        return start_idx







       

        