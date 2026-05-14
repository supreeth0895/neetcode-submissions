#SUPREETH
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set()

        for num in nums:
            my_set.add(num)
        
        starting_numbers_list = []
        for num in my_set:
            if num-1 not in my_set:
                starting_numbers_list.append(num)

        print(starting_numbers_list)
        #HINT2: Is there any way to identify the start of a sequence?
        #For example, in [1, 2, 3, 10, 11, 12], only 1 and 10 are the beginning of a sequence.
        #Instead of trying to form a sequence for every number, we should only consider numbers like 1 and 10.
        max_len = 0
        for num in starting_numbers_list:
            cur_num = num
            while cur_num in my_set:
                cur_num = cur_num+1
            
            max_len = max(max_len, cur_num-num)

        return max_len

        


          





        