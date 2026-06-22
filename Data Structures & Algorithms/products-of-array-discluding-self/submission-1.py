class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1]
        right_product = [1]
        for i in range(1, len(nums)):
            left_product.append(left_product[i-1]*nums[i-1])
        nums = nums[::-1]
        for i in range(1, len(nums)):
            right_product.append(right_product[i-1]*nums[i-1])
        res = []
        right_product = right_product[::-1]
        for i in range(len(right_product)):
            res.append(left_product[i]*right_product[i])
        return res