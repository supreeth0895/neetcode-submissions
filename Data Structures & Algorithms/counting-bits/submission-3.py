class Solution:
    def countBits(self, n: int) -> List[int]:
        my_map = {0:0, 1:1}
        power = 1
        offset =0
        num = 2**power + offset
        
        while num <=n:
            # Conver num to 2 power n + Offset format:
            if num == 2**(power+1):
                power = power+1
                offset = 0
            
            #Make the power th bit as 0 : ie; [0-1] - 1st bit from right, for [2-4] 2nd bit from right, for [5-8] - 3rd bit from right, [9-16] - 4th bit from right
            new_num1 = 1
            new_num1 = new_num1 << power
            new_num1 = ~new_num1
            new_num1 = num & new_num1

            #Now, this should be a number we have already computed before. We add 1 because we just set powerth bit to 1
            total_count = my_map[new_num1] + 1
            my_map[num] = total_count
            num = num+1
            offset = offset+1


        #return answer
        answer = []
        for num in range(0,n+1): 
            answer.append(my_map[num])
        return answer