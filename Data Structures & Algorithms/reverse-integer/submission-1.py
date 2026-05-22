class Solution:
    def reverse(self, x: int) -> int:
        new_num = 0
        temp = abs(x)
        while temp>= 10:
            digit = temp%10
            temp = math.trunc(temp/10)
            new_num = new_num*10 + digit
        
        if new_num == 214748364:
            if x >= 0:
                if temp<=7:
                    digit = temp%10
                    temp = math.trunc(temp/10)
                    new_num = new_num*10 + digit
                    return new_num
                else:
                    return 0
            else:
                if temp<=8:
                    digit = temp%10
                    temp = math.trunc(temp/10)
                    new_num = new_num*10 + digit
                    return -new_num
                else:
                    return 0
            
        elif new_num < 214748364:
            digit = temp%10
            temp = math.trunc(temp/10)
            new_num = new_num*10 + digit
            if x >= 0:
                return new_num
            else:
                return -new_num

        return 0








        



