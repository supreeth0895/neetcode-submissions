class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        #num of bananas koko can eat per hour  (eating speed) will be from min(piles[i]) to max(piles[i])
        #Check for mid value eating speed.
        #If time taken > h
            #then increase the speed
        #If time taken ==h:
            #then it is perfect
        #if time taken < h:
            #then decrease speed lower than mid.
            #Also, in this case, Keep tack of minimum difference from h.
            #The speed which has least deviation from h, is the optimal speed
        
        start = 1
        end = max(piles)

        current_best_speed = end

        while start<=end:
            mid_speed = (start+end)//2
            hrs = self.hours_taken(mid_speed, piles)
            if hrs <= h:
                current_best_speed = mid_speed
                end = mid_speed -1
            else:
                start = mid_speed +1
        return current_best_speed

    def hours_taken(self, speed, piles):
        h = 0
        for pile in piles:
            h = h + (math.ceil(pile/speed))
        return h
