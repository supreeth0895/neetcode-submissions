#SUPREETH
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        sum = numbers[left] + numbers[right]

        while left<right:
            if sum == target:
                return [left+1, right+1]
            if sum > target :
                right = right -1
            else:
                left =left+1
            sum = numbers[left] + numbers[right]
            
            
        

        return []
            

        