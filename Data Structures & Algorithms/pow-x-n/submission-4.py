class Solution:
    def myPow(self, x: float, n: int) -> float:
        abs_n = abs(n)
        def helper(val, cur_pow):
            if cur_pow == 1:
                return val
            if cur_pow == 0:
                return 1
            if cur_pow %2 == 0:
                return helper(val*val, cur_pow//2)
            else:
                return val*helper(val*val, (cur_pow-1)//2) # basically 10^5 = (10* ((10^2)^2)
        
        answer = helper(x,abs_n)
        if n >=0:
            return answer
        return 1/answer




#O(n)
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

                


        