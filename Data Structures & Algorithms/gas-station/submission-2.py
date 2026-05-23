#SUPREETH
# SUMMARY:
# We want to find the starting station index that allows us to complete
# a full circuit. Two key observations drive this solution:
#   1. If total gas < total cost, no solution exists → return -1
#   2. If a solution exists, it is unique. We find it greedily:
#      scan stations left to right, tracking a running fuel balance.
#      Whenever the balance goes negative, every station from the last
#      candidate start up to the current one is disqualified, so we
#      reset the balance and move our candidate start forward.
#      The global sum check guarantees the final candidate is valid.

# If total gas available is less than total cost to travel,
# it's impossible to complete the circuit regardless of starting point

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        # Calculate net gas gain/loss at each station:
        # positive = we gain fuel here, negative = we lose fuel here
        gas_left_for_index = [0] * len(gas)
        for i in range(0, len(gas)):
            gas_left_for_index[i] = gas[i] - cost[i]

        cur_total = 0  # Running fuel tank balance from our chosen start point
        start_idx = 0  # Our candidate starting station
        for i in range(0, len(gas)):
            # If tank went negative, the current start_idx (and every station
            # between it and i) cannot be a valid start — we would have run out
            # of fuel before reaching i. Reset and try starting from i instead.
            if cur_total < 0:
                cur_total = 0
                start_idx = i
            cur_total = cur_total + gas_left_for_index[i]

        # Since we already confirmed a solution exists (sum check above),
        # start_idx is guaranteed to be the unique valid starting station
        return start_idx






       

        