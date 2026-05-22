# SUPREETH
class Solution:
    def isHappy(self, n: int) -> bool:
        
        def helper(n, visited):
            # Cycle detected — this number is not happy
            if n in visited:
                return False
            
            # Base case: reached 1, the number is happy
            if n == 1:
                return True
            
            # Compute the sum of squares of each digit
            temp = n
            sum_of_squares = 0
            while temp:
                digit = temp % 10          # Extract the last digit
                temp = temp // 10          # Remove the last digit
                sum_of_squares += digit ** 2
            
            # Mark current number as visited before recursing
            visited.add(n)
            
            # Recurse with the new transformed number
            return helper(sum_of_squares, visited)
        
        return helper(n, set())