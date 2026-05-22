class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(n,visited):
            if n in visited:
                return False
            if n == 1:
                return True
            temp = n
            sum_of_squares = 0
            while temp:
                digit = temp%10
                temp= temp//10
                sum_of_squares = sum_of_squares + (digit**2)

            visited.add(n)
            ret_val = helper(sum_of_squares,visited)
            return ret_val


        return helper(n, set())