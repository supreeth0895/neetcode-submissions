class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        # Build frequency map manually (expanding Counter)
        count = {}
        for card in hand:
            if card in count:
                count[card] += 1
            else:
                count[card] = 1
        
        for num in hand:
            # Find start of this group by going left
            start = num
            while start in count:
                start -= 1
            
            # Form all groups starting from 'start'
            while start <= num:
                while count.get(start, 0):
                    # Try to form one group of groupSize consecutive cards
                    for i in range(start, start + groupSize):
                        if not count.get(i, 0):
                            return False
                        count[i] -= 1
                        if count[i] == 0:
                            del count[i]  # clean up empty entries
                start += 1
        
        return True