class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a_match,b_match,c_match = False,False,False

        for triplet in triplets:
            if target[0] >= triplet[0] and target[1] >= triplet[1] and target[2] >= triplet[2]:
                if target[0] == triplet[0]:
                    a_match = True
                if target[1] == triplet[1]:
                    b_match = True
                if target[2] == triplet[2]:
                    c_match = True
            #otherwise that triplet is unusable.
        return a_match and b_match and c_match




        