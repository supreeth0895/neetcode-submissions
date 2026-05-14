#SUPREETH
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        i=0
        for num in nums:
            if num not in my_map:
                my_map[num] =[i]
            else:
                my_map[num].append(i)
            i=i+1
        i=0
        for num in nums:
            if target-num != num:
                if ((target-num) in my_map) :
                    return [my_map[num][0], my_map[(target-num)][0]]
            if target-num == num:
                if (num in my_map) and len(my_map[num]) > 1:
                    return [my_map[num][0], my_map[num][1]]
        
                



        