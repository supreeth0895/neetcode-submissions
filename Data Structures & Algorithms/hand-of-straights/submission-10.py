#SUPREETH
#Heap + hashing:
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True


#O(n) - Too hard to implement

# class Solution:
#     def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
#         if len(hand) % groupSize != 0:
#             return False
        
#         my_map = {}

#         for num in hand:
#             if num in my_map:
#                 my_map[num] = my_map[num] + 1
#             else:
#                 my_map[num] = 1
        
#         print(my_map)
        
#         for num in hand:
#                 if my_map[num] == 0:
#                     continue
#                 #Get the left val(Start_val) of the range in which this number would exist:
#                 left_start_val = num-1
#                 while left_start_val in my_map and my_map[left_start_val] > 0 :
#                     left_start_val = left_start_val -1
#                 left_start_val = left_start_val+1
#                 print(my_map)

#                 while left_start_val in my_map and my_map[left_start_val] > 0 and  left_start_val+groupSize <= num :
#                     temp = left_start_val
#                     count = 0
#                     while my_map.get(temp, 0) != 0 and count < groupSize:
#                         print(temp)
#                         my_map[temp] = my_map[temp]-1
#                         temp = temp+1
#                         count = count+1
#                         print(count)
#                     if count != groupSize:
#                         print(count)
#                         return False
#                     left_start_val = left_start_val +1

#         return True