# Approach: Grade-School Multiplication (Long Multiplication)
# Multiply num2 digit by digit against the entire num1, exactly as done by hand.
# Each partial product is shifted left by its position (trailing zeros added).
# All partial products are then summed column by column from right to left.
#
# Example: 111 * 222
#   Step 1 - partial products:
#     111 * 2 (ones place)   =  222        -> "222"
#     111 * 2 (tens place)   =  222 + "0"  -> "2220"
#     111 * 2 (hundreds)     =  222 + "00" -> "22200"
#   Step 2 - column-wise sum:
#       222
#      2220
#    +22200
#    ------
#     24642
#
# All arithmetic is done on strings to support 200+ digit inputs.
# Time: O(m*n) where m, n are the lengths of num1 and num2.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        right1 = len(num1) - 1
        right2 = len(num2) - 1

        products = []  # Stores each partial product as a string (with trailing zeros)

        # ── Phase 1: compute partial products ──────────────────────────────────
        for i in range(right2, -1, -1):  # Iterate digits of num2 right to left
            ch_digit1 = ord(num2[i]) - ord('0')
            carry = 0
            total_prod = ""

            for j in range(right1, -1, -1):  # Multiply current num2 digit by all of num1
                ch_digit2 = ord(num1[j]) - ord('0')
                temp_prod = (ch_digit1 * ch_digit2) + carry
                carry = temp_prod // 10          # Tens digit carried to next column
                temp_prod_digit = temp_prod % 10  # Ones digit written into result
                total_prod = str(temp_prod_digit) + total_prod

            if carry:  # Any leftover carry becomes the leading digit
                total_prod = str(carry) + total_prod

            products.append(total_prod)

        # ── Phase 2: shift each partial product left by its row index ──────────
        # Row 0 (ones place of num2)      -> no shift
        # Row 1 (tens place of num2)      -> one trailing zero
        # Row 2 (hundreds place of num2)  -> two trailing zeros  ... etc.
        max_product_len = 0
        for i in range(len(products)):
            products[i] += "0" * i                          # Append i trailing zeros
            max_product_len = max(max_product_len, len(products[i]))

        # At this point products looks like (for 111 * 222):
        #   ["222", "2220", "22200"]

        # ── Phase 3: add all partial products column by column ─────────────────
        # Each column sums at most one digit from each product string.
        # With inputs up to 200 digits, the max column sum is 9*200 = 1800,
        # so a single carry variable is always sufficient.
        carry = 0
        answer = ""

        for i in range(max_product_len):  # Iterate columns right to left
            col_sum = carry  # Start with carry from the previous column

            for product in products:
                # Index from the right: position i from the end
                idx = len(product) - 1 - i
                if idx >= 0:
                    col_sum += ord(product[idx]) - ord('0')

            carry = col_sum // 10       # Carry into the next column
            answer = str(col_sum % 10) + answer  # Current column's digit

        # If a final carry remains after processing all columns, prepend it
        if carry:
            answer = str(carry) + answer

        return answer