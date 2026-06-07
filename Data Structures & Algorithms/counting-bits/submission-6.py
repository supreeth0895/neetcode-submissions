class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = [0,1]
        cur_max = 1
        while cur_max < n:
            cur_max = cur_max*2
            temp = answer[:]
            for i in range(0, len(temp)):
                answer.append(temp[i]+1)
        return answer[:n+1]
                

# 0
# 1
# 01
# 10
# 100
# 101
# 110
# 111
        