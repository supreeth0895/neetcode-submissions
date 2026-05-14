#SUPREETH
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = math.trunc((start+ end)/2)
            if target == nums[mid]:
                return mid
            elif nums[start] < nums[mid]:
                if target >= nums[start] and target <= nums[mid-1]:
                    end = mid-1
                else:
                    start = mid+1
            else:
                if mid+1 < len(nums) and target >= nums[mid+1] and target <= nums[end]:
                    start = mid+1
                else:
                    end = mid-1
        return -1

        