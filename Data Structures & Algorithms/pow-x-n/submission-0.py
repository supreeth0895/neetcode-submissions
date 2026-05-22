class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            ans = 1
            for i in range(0,n):
                ans = ans*x
            return ans
        else:
            ans = 1.0
            for i in range(0,-n):
                ans = ans/x
            return ans

                


        