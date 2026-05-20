class Solution:
    def countBits(self, n: int) -> List[int]:
        my_map = {0:0, 1:1}
        power = 1
        offset =0
        num = 2**power + offset
        
        while num <=n:
            if num == 2**(power+1):
                power = power+1
                offset = 0
            print(power,"-", offset )
            #Make the leftmost bit as 0
            new_num1 = 1
            new_num1 = new_num1 << power
            
            new_num1 = ~new_num1

            new_num1 = num & new_num1
            print(new_num1)

            #Now, this should be a number we have already computer before.
            total_count = my_map[new_num1] + 1
            print(num ,"=====" ,total_count)
            my_map[num] = total_count
            num = num+1
            offset = offset+1


        #return answer
        answer = []
        for num in range(0,n+1): 
            answer.append(my_map[num])
        return answer