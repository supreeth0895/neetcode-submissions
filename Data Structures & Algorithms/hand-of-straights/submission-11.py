#O(n) Algorithm:
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        
        for num in hand:
            # Find start of this group by going left
            start = num
            while count[start - 1]:
                start -= 1
            
            # Form all groups starting from 'start'
            while start <= num:
                while count[start]:
                    # Try to form one group of groupSize consecutive cards
                    for i in range(start, start + groupSize):
                        if not count[i]:
                            return False
                        count[i] -= 1
                start += 1
        
        return True
            