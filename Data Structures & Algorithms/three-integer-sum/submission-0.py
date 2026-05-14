class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        my_map = {}
        for i, num in enumerate(nums):
            if num in my_map:
                my_map[num].append(i)
            else:
                my_map[num] = [i]
        
        ans = set()

        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                target = -1* (nums[i]+ nums[j])

                if target in  my_map:
                    for val in my_map[target]:
                        if val > i and val > j :
                            ans.add(tuple(sorted([nums[i],nums[j],nums[val]])))
        

         

        return list(ans)




        
            


        