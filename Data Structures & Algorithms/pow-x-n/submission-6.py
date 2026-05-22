# Approach: Fast Power (Exponentiation by Squaring)
# Instead of multiplying x by itself n times (O(n)), we use the following rules:
#   - If power is even: x^n = (x^2)^(n/2)      e.g. 10^4 = (10^2)^2 = 100^2
#   - If power is odd:  x^n = x * (x^2)^((n-1)/2) e.g. 10^5 = 10 * (10^2)^2
# This halves the problem size each call, giving O(log n) time complexity.
# Negative exponents are handled by computing the positive version, then taking 1/answer.

class Solution:
    def myPow(self, x: float, n: int) -> float:
        abs_n = abs(n)  # Work with positive exponent; handle negatives at the end

        def helper(val, cur_pow):
            if cur_pow == 0:  # Base case: anything^0 = 1
                return 1
            if cur_pow == 1:  # Base case: anything^1 = itself
                return val
            if cur_pow % 2 == 0:
                # Even power: square the base and halve the exponent
                # e.g. x^4 = (x^2)^2
                return helper(val * val, cur_pow // 2)
            else:
                # Odd power: peel off one x, then apply even rule to the rest
                # e.g. x^5 = x * (x^2)^2
                return val * helper(val * val, (cur_pow - 1) // 2)

        answer = helper(x, abs_n)

        if n >= 0:
            return answer
        return 1 / answer  # x^(-n) = 1 / x^n




#O(n) - This was the solution I inititally came up with. But this is O(n) TC - Not really useful
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n >= 0:
#             ans = 1
#             for i in range(0,n):
#                 ans = ans*x
#             return ans
#         else:
#             ans = 1.0
#             for i in range(0,-n):
#                 ans = ans/x
#             return ans

                


        