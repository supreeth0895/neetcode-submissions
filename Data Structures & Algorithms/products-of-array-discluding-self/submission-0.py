class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i, left_product, right_product = 1, [1], [1]
        while i < len(nums):
            left_product.append(left_product[i-1]*nums[i-1])
            i+=1
        nums = nums[::-1]
        i = 1
        while i < len(nums):
            right_product.append(right_product[i-1]*nums[i-1])
            i+=1
        right_product = right_product[::-1]
        res = []
        for i in range(len(left_product)):
            res.append(left_product[i]*right_product[i])
        return res