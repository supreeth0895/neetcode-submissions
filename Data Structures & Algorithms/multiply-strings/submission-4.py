class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 =="0":
            return "0"
        right1 = len(num1) - 1
        right2 = len(num2) -1

        prod_count = 0
        products = []

        for i in range(right2, -1,-1):
            ch = num2[i] #See if this needs to be done in a different way
            ch_digit1 = ord(ch) -ord('0')
            carry = 0
            temp_prod = 0
            total_prod = ""

            for j in range(right1, -1,-1):
                ch2 = num1[j]
                ch_digit2 = ord(ch2) - ord('0')
                temp_prod = (ch_digit1 * ch_digit2) + carry
                if temp_prod >= 10:
                    carry = temp_prod//10
                    temp_prod_digit = temp_prod%10
                else:
                    carry = 0
                    temp_prod_digit = temp_prod
                total_prod =  str(temp_prod_digit) + total_prod
            if carry:
                total_prod =  str(carry) + total_prod


            products.append(total_prod)
            prod_count = prod_count+1
        
        max_product_len = 0
        for i in range(0, len(products)):
            for j in range(0,i):
                products[i] = products[i] +"0"
            max_product_len = max(max_product_len, len(products[i]))

        #   At this Point we will have all the products like this in string because length can be 200+ chars  . 
        #     111
        #     222
        #     ---
        #     222
        #    2220
        #   22200
        # To Confirm you can Print Products:
        # print(products)

        #Now it's time to Add up Products which are stored as string. We need to add them all up digit by digit. We cannot directly add them up. Each num may be 200+ chars.
        carry_to_next_digit = 0
        carry_to_next_next_digit = 0
        carry_to_next_next_next_digit = 0
        answer = ""
        for i in range(0, max_product_len):
            total_sum = 0
            for j in range(0, len(products)):
                my_str = products[j]
                if len(my_str)-1-i >= 0:
                    total_sum = total_sum + (ord(my_str[len(my_str)-1-i]) - ord('0')) 
            total_sum = total_sum + carry_to_next_digit

            digit = total_sum%10
            answer = str(digit) + answer 

            carry_to_next_next_next_digit = carry_to_next_next_digit
            carry_to_next_next_digit = carry_to_next_digit
            carry_to_next_digit = 0
            
            if total_sum <= 99:
                carry_to_next_digit = total_sum//10
            elif total_sum <= 999:
                carry_to_next_digit = total_sum//10
                carry_to_next_next_digit = carry_to_next_next_digit + total_sum//100
            else:
                carry_to_next_digit = total_sum//10
                carry_to_next_next_digit = carry_to_next_next_digit + (total_sum//100)
                carry_to_next_next_next_digit = carry_to_next_next_next_digit + (total_sum//1000)


        while carry_to_next_digit:
            answer = str(carry_to_next_digit) + answer
            carry_to_next_next_next_digit = carry_to_next_next_digit
            carry_to_next_next_digit = carry_to_next_digit
            carry_to_next_digit = 0

        return answer