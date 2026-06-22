class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        number_bananas = math.inf
        piles = sorted(piles)
        l = 1
        r = piles[-1]
        self.hours = h
        self.piles = piles
        while l <= r:
            pivot = (l+r)//2
            if self.get_number(pivot)<=h:
                number_bananas = min(pivot, number_bananas)
                r = pivot-1
            elif self.get_number(pivot)>h:
                l = pivot+1
        return number_bananas

    def get_number(self, number):
        result = 0
        for elem in self.piles:
            result+= math.ceil(elem/number)
        return result