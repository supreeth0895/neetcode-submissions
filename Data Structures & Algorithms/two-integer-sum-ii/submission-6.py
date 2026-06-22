class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 1, len(numbers)
        while i < j:
            if numbers[i-1]+numbers[j-1] > target:
                j-=1
                continue
            elif numbers[i-1]+numbers[j-1] < target:
                i+=1
                continue
            else:
                return [i,j]
        