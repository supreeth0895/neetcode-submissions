#SUPREETH
#nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.
#Make use of this. To mark nums[i] as visited, mark the number at index nums[i] negetive.
#So if you encounter another nums[i], we see that negetive sign and relaize that this is repeated
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            if nums[abs(nums[i])] > 0:
               nums[abs(nums[i])] = nums[abs(nums[i])] * -1
            else:
                return abs(nums[i])


#But We are NOT ALLOWED TO MODIFY THE ARRAY:

#USE FAST AND SLOW POINTERS
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # PHASE 1: Detect the cycle and find a meeting point inside it.
        # We treat the array like a linked list: from index i, the "next"
        # index is nums[i]. Because a value is duplicated, two indices point
        # to the same place -> the chain must contain a cycle.
        slow, fast = 0, 0
        while True:
            slow = nums[slow]            # tortoise: advances 1 step
            fast = nums[nums[fast]]      # hare: advances 2 steps
            if slow == fast:             # guaranteed to happen inside the cycle
                break
        # When we break, slow == fast at SOME point in the cycle.
        # This point is NOT necessarily the duplicate -- it's just where the
        # two pointers happened to collide. We still need the cycle's ENTRANCE.

        # PHASE 2: Find the cycle entrance (= the duplicate number).
        # Key fact (provable with algebra): the distance from index 0 to the
        # entrance equals the distance from the meeting point to the entrance.
        # So restart one pointer at 0, keep the other at the meeting point,
        # and move BOTH one step at a time -- equal speed this time.
        slow2 = 0
        while True:
            slow = nums[slow]            # continues from the meeting point
            slow2 = nums[slow2]          # walks from the start, same speed
            if slow == slow2:            # they meet exactly at the entrance
                return slow              # the entrance index is the duplicate