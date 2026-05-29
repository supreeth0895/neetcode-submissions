class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1,nums2
        if len(B) < len(A):
            A,B = B,A
        left_idx = 0
        right_idx = len(A)-1

        total_len = len(A)+len(B)
        half_len = total_len//2

        while True:
            midA = (left_idx+right_idx)//2
            midB = (half_len-1) -  (midA+1)


            if midA >= 0:
                left_val_A = A[midA]
            else:
                left_val_A = float("-inf")


            if midA+1 < len(A):
                right_val_A = A[midA+1]
            else:
                right_val_A = float("inf")
            
            if midB >= 0:
                left_val_B = B[midB]
            else:
                left_val_B = float("-inf")


            if midB+1 < len(B):
                right_val_B = B[midB+1]
            else:
                right_val_B = float("inf")
            
            if left_val_A <= right_val_B and left_val_B <= right_val_A:
                #then the split is correct. compute and return median:

                #if combined array is odd length
                if (len(A)+len(B)) %2 != 0:
                    return min(right_val_A, right_val_B)    


                #Even length
                else:
                    return (max(left_val_A,left_val_B) + min(right_val_A,right_val_B))/2
            elif left_val_A > right_val_B:
                right_idx = midA-1
            else: 
                left_idx = midA+1