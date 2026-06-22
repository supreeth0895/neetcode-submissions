class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        res = set()
        for x in range(len(nums)):
            i = x+1
            j = len(nums)-1
            while i < j:
                if nums[i]+nums[j]>(0-nums[x]):
                    j-=1
                    continue
                elif nums[i]+nums[j]< 0-nums[x]:
                    i+=1
                    continue
                elif nums[i]+nums[j]+nums[x] == 0:
                    res.add((nums[x], nums[i], nums[j]))
                i+=1
                j-=1
        return [list(tup) for tup in res]