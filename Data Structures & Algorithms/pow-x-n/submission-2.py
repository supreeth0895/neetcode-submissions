class Solution:
    def myPow(self, x: float, n: int) -> float:
        abs_n = abs(n)
        my_map = {}
        def helper(val, cur_pow):
            if cur_pow == n:
                return val
            elif 2*cur_pow <= abs_n:
                return helper(val*val, 2*cur_pow)
            else:
                for i in range(0,abs_n-cur_pow):
                    val = val*x
                return val
        
        if n == 0:
            return 1
        ret_val = helper(x,1)
        if n < 0 :
            return 1/ret_val
        else:
            return ret_val




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

                


        