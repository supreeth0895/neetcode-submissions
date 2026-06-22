class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        cnt = 0
        res = math.inf
        for i in range(k):
            if blocks[i] == 'W':
                cnt+=1
        res = min(res, cnt)
        for r in range(k, len(blocks)):
            if blocks[r-k] == 'W':
                cnt-=1
            if blocks[r] == 'W':
                cnt+=1
            res = min(res, cnt)
        #res = min(res, cnt)
        return res