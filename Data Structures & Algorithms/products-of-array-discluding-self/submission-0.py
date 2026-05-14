class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1]*len(nums)
        right_product = [1]*len(nums)

        for i in range(0,len(nums)):
            if i == 0 :
                left_product[i] = 1
            elif i == 1:
                left_product[i] = nums[0]
            else:
                left_product[i] = left_product[i-1]*nums[i-1]
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1 :
                right_product[i] = 1
            elif i == len(nums) - 2 :
                right_product[i] = nums[len(nums)-1]
            else:
                right_product[i] = right_product[i+1]*nums[i+1]
        print(left_product)
        print(right_product)
        product_except_self = [1]*len(nums)

        for i in range(0,len(nums)):
            product_except_self[i] = left_product[i]*right_product[i]
        return product_except_self