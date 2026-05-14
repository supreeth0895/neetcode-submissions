class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
    
        def backtrack(i, total, combo):
            if i == len(nums):
                return
            if total > target:
                return
            if total == target:
                ans.add(tuple(combo))
                return
            
            backtrack(i+1, total, combo)

            new_combo1 = combo[:]
            new_combo1.append(nums[i])
            backtrack(i, total+nums[i] , new_combo1)
            new_combo2 = combo[:]
            new_combo2.append(nums[i])
            backtrack(i+1, total+nums[i] , new_combo2)
        
        backtrack(0,0,[])
        result = [list(item) for item in ans]

        return result